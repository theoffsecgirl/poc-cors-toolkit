#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""cors-scanner v2.0 - Advanced CORS Misconfiguration Scanner

CLI scanner for detecting CORS misconfigurations across multiple targets.
Complements the HTML toolkit with automated scanning capabilities.
"""

import argparse
import json
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass, asdict
from typing import List, Dict, Optional
from urllib.parse import urlparse

import requests
from colorama import Fore, Style, init
from tqdm import tqdm

init(autoreset=True)


@dataclass
class ScanConfig:
    url: Optional[str] = None
    url_list: Optional[str] = None
    method: str = "GET"
    auth_header: Optional[str] = None
    body: Optional[str] = None
    threads: int = 10
    timeout: int = 10
    json_output: Optional[str] = None
    verbose: bool = False


@dataclass
class CORSFinding:
    url: str
    origin: str
    method: str
    status_code: int
    acao_header: Optional[str]
    acac_header: Optional[str]
    vulnerabilities: List[str]
    severity: str
    timestamp: float


class CORSScanner:
    
    ORIGIN_TESTS = [
        "https://evil.com",
        "null",
        "http://localhost",
        "file://",
        "data:text/html",
    ]
    
    def __init__(self, config: ScanConfig):
        self.config = config
        self.findings: List[CORSFinding] = []
        self.session = requests.Session()
        self._setup_session()
    
    def _setup_session(self):
        headers = {"User-Agent": "Mozilla/5.0 (compatible; cors-scanner/2.0)"}
        if self.config.auth_header:
            key, value = self.config.auth_header.split(":", 1)
            headers[key.strip()] = value.strip()
        self.session.headers.update(headers)
    
    def log_info(self, msg: str):
        print(f"{Fore.GREEN}[+] {msg}{Style.RESET_ALL}")
    
    def log_warn(self, msg: str):
        print(f"{Fore.YELLOW}[!] {msg}{Style.RESET_ALL}")
    
    def log_error(self, msg: str):
        print(f"{Fore.RED}[x] {msg}{Style.RESET_ALL}")
    
    def log_verbose(self, msg: str):
        if self.config.verbose:
            print(f"{Fore.CYAN}[~] {msg}{Style.RESET_ALL}")
    
    def log_vuln(self, msg: str, severity: str = "high"):
        color = Fore.RED if severity == "critical" else Fore.YELLOW if severity == "medium" else Fore.CYAN
        print(f"{color}[!] VULNERABLE: {msg}{Style.RESET_ALL}")
    
    def build_targets(self) -> List[str]:
        targets = []
        
        if self.config.url:
            targets.append(self.config.url.strip())
        
        if self.config.url_list:
            try:
                with open(self.config.url_list, "r", encoding="utf-8") as f:
                    for line in f:
                        line = line.strip()
                        if line and not line.startswith("#"):
                            targets.append(line)
            except OSError as e:
                self.log_error(f"Error leyendo lista de URLs: {e}")
                sys.exit(1)
        
        if not targets:
            self.log_error("No se proporcionaron objetivos válidos")
            sys.exit(1)
        
        return list(dict.fromkeys(targets))
    
    def generate_origins(self, url: str) -> List[str]:
        """Generate origin variations for testing"""
        try:
            parsed = urlparse(url)
            host = parsed.hostname
            protocol = parsed.scheme
            
            origins = list(self.ORIGIN_TESTS)
            origins.extend([
                f"{protocol}://{host}",
                f"https://{host}.attacker.com",
                f"https://attacker.{host}",
                f"https://sub.{host}",
                f"http://{host}",
            ])
            
            return origins
        except Exception:
            return self.ORIGIN_TESTS
    
    def analyze_vulnerability(self, url: str, origin: str, headers: Dict, status: int) -> tuple[List[str], str]:
        """Analyze response for CORS misconfigurations"""
        acao = headers.get('access-control-allow-origin', '').lower()
        acac = headers.get('access-control-allow-credentials', '').lower()
        
        vulns = []
        severity = "low"
        
        if acao == origin.lower() and origin.lower() != urlparse(url).netloc.lower():
            vulns.append("Dynamic origin reflection")
            severity = "high"
        
        if acao == '*':
            vulns.append("Wildcard (*) allowed")
            severity = "medium"
        
        if acao == 'null':
            vulns.append("Null origin accepted")
            severity = "high"
        
        if acac == 'true' and acao and acao != urlparse(url).netloc.lower():
            vulns.append("Credentials + Origin reflection (CRITICAL)")
            severity = "critical"
        
        if origin.startswith('file://') and acao == origin.lower():
            vulns.append("File protocol accepted")
            severity = "high"
        
        if origin.startswith('data:') and acao == origin.lower():
            vulns.append("Data URI accepted")
            severity = "high"
        
        return vulns, severity
    
    def test_single(self, url: str, origin: str) -> Optional[CORSFinding]:
        """Test single URL with specific origin"""
        headers = {"Origin": origin}
        
        try:
            if self.config.method == "GET":
                resp = self.session.get(
                    url,
                    headers=headers,
                    timeout=self.config.timeout,
                    verify=True
                )
            else:
                resp = self.session.request(
                    self.config.method,
                    url,
                    headers=headers,
                    data=self.config.body,
                    timeout=self.config.timeout,
                    verify=True
                )
            
            response_headers = {k.lower(): v for k, v in resp.headers.items()}
            
            vulns, severity = self.analyze_vulnerability(url, origin, response_headers, resp.status_code)
            
            if vulns:
                finding = CORSFinding(
                    url=url,
                    origin=origin,
                    method=self.config.method,
                    status_code=resp.status_code,
                    acao_header=response_headers.get('access-control-allow-origin'),
                    acac_header=response_headers.get('access-control-allow-credentials'),
                    vulnerabilities=vulns,
                    severity=severity,
                    timestamp=time.time()
                )
                
                self.log_vuln(f"{url} with origin {origin}", severity)
                for vuln in vulns:
                    print(f"    - {vuln}")
                
                return finding
            
            self.log_verbose(f"✓ {url} with {origin}: No vulnerability")
            
        except requests.RequestException as e:
            self.log_verbose(f"Error testing {url}: {e}")
        
        return None
    
    def scan_target(self, url: str) -> List[CORSFinding]:
        """Scan single target with multiple origins"""
        findings = []
        origins = self.generate_origins(url)
        
        for origin in origins:
            finding = self.test_single(url, origin)
            if finding:
                findings.append(finding)
        
        return findings
    
    def scan(self) -> Dict:
        """Main scan routine"""
        print(f"{Fore.CYAN}╭────────────────────────────────────────────╮{Style.RESET_ALL}")
        print(f"{Fore.CYAN}│  cors-scanner v2.0 - CORS Misconfiguration │{Style.RESET_ALL}")
        print(f"{Fore.CYAN}╰────────────────────────────────────────────╯{Style.RESET_ALL}\n")
        
        targets = self.build_targets()
        self.log_info(f"Objetivos cargados: {len(targets)}")
        
        all_findings = {}
        
        for target in tqdm(targets, desc="Escaneando", unit="url"):
            findings = self.scan_target(target)
            if findings:
                all_findings[target] = findings
        
        return self.generate_report(all_findings, targets)
    
    def generate_report(self, all_findings: Dict, targets: List[str]) -> Dict:
        """Generate comprehensive report"""
        total_vulns = sum(len(v) for v in all_findings.values())
        
        print("\n" + "="*60)
        self.log_info("Escaneo completado")
        print(f"    Objetivos analizados: {len(targets)}")
        print(f"    URLs vulnerables: {len(all_findings)}")
        print(f"    Vulnerabilidades totales: {total_vulns}")
        
        # Severity breakdown
        severity_count = {"critical": 0, "high": 0, "medium": 0, "low": 0}
        for findings in all_findings.values():
            for f in findings:
                severity_count[f.severity] = severity_count.get(f.severity, 0) + 1
        
        if total_vulns > 0:
            print(f"\n    Por severidad:")
            print(f"      - {Fore.RED}Critical{Style.RESET_ALL}: {severity_count['critical']}")
            print(f"      - {Fore.RED}High{Style.RESET_ALL}: {severity_count['high']}")
            print(f"      - {Fore.YELLOW}Medium{Style.RESET_ALL}: {severity_count['medium']}")
            print(f"      - {Fore.CYAN}Low{Style.RESET_ALL}: {severity_count['low']}")
        
        report = {
            "scanner_version": "2.0",
            "targets_scanned": len(targets),
            "vulnerable_urls": len(all_findings),
            "total_vulnerabilities": total_vulns,
            "severity_summary": severity_count,
            "findings": {
                target: [asdict(f) for f in findings]
                for target, findings in all_findings.items()
            }
        }
        
        return report
    
    def export_json(self, report: Dict):
        """Export report to JSON"""
        if not self.config.json_output:
            return
        
        try:
            with open(self.config.json_output, "w", encoding="utf-8") as f:
                json.dump(report, f, indent=2, ensure_ascii=False)
            self.log_info(f"Resultados guardados en {self.config.json_output}")
        except OSError as e:
            self.log_error(f"Error guardando JSON: {e}")


def parse_args():
    parser = argparse.ArgumentParser(
        description="cors-scanner v2.0 - Advanced CORS Misconfiguration Scanner",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    parser.add_argument("-u", "--url", help="URL objetivo")
    parser.add_argument("-L", "--list", help="Archivo con lista de URLs")
    parser.add_argument("-m", "--method", default="GET", help="Método HTTP (default: GET)")
    parser.add_argument("--auth-header", help="Header de autenticación (ej: 'Authorization: Bearer token')")
    parser.add_argument("--body", help="Body para POST/PUT")
    parser.add_argument("-T", "--threads", type=int, default=10, help="Número de threads (default: 10)")
    parser.add_argument("-t", "--timeout", type=int, default=10, help="Timeout en segundos (default: 10)")
    parser.add_argument("-o", "--json-output", help="Guardar resultados en JSON")
    parser.add_argument("-v", "--verbose", action="store_true", help="Modo verbose")
    
    args = parser.parse_args()
    
    if not args.url and not args.list:
        parser.error("Debes proporcionar --url o --list")
    
    return args


def main():
    args = parse_args()
    
    config = ScanConfig(
        url=args.url,
        url_list=args.list,
        method=args.method,
        auth_header=args.auth_header,
        body=args.body,
        threads=args.threads,
        timeout=args.timeout,
        json_output=args.json_output,
        verbose=args.verbose
    )
    
    scanner = CORSScanner(config)
    
    try:
        report = scanner.scan()
        scanner.export_json(report)
    except KeyboardInterrupt:
        scanner.log_warn("Interrumpido por el usuario")
        sys.exit(1)


if __name__ == "__main__":
    main()
