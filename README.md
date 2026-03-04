# CORS Toolkit v2.0

Herramienta completa para auditar y detectar misconfigurations de CORS (Cross-Origin Resource Sharing).

Incluye toolkit HTML interactivo y CLI scanner para automatización.

---

## 🚀 Novedades v2.0 (2026)

### Toolkit HTML Mejorado
- ✅ **Detección automática de vulnerabilidades**
- ✅ **10 origin variations** predefinidos por target
- ✅ **Análisis de severidad** (Critical/High/Medium/Low)
- ✅ **Progress bars** para escaneos masivos
- ✅ **Export a archivo** con timestamp
- ✅ **Copy to clipboard** integrado
- ✅ **UI moderna** con dark theme

### CLI Scanner (Nuevo)
- ✅ **Escaneo automatizado** de múltiples URLs
- ✅ **JSON reporting** estructurado
- ✅ **Threading** para velocidad
- ✅ **Severity classification**
- ✅ **Verbose mode** para debugging

---

## 📦 Instalación

### Toolkit HTML (Sin instalación)

Solo abre el archivo en el navegador:

```bash
git clone https://github.com/theoffsecgirl/poc-cors-toolkit.git
cd poc-cors-toolkit
firefox index.html  # o chrome index.html
```

### CLI Scanner

```bash
git clone https://github.com/theoffsecgirl/poc-cors-toolkit.git
cd poc-cors-toolkit
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

## 🔥 Uso - Toolkit HTML

### Prueba Individual

1. Introduce la **URL objetivo**
2. Selecciona un **Origin** (o prueba todos)
3. Configura **método HTTP** y headers
4. Click en **▶️ Prueba Individual**

### Escaneo Masivo

1. Pega lista de URLs en **📋 Lista de URLs**
2. Selecciona origin
3. Click en **🔄 Probar Lista Completa**
4. **💾 Exportar Resultados** cuando termine

### Probar Todos los Origins

1. Introduce URL objetivo
2. Click en **🎯 Probar Todos los Origins**
3. Automáticamente prueba 10 variaciones

---

## 💻 Uso - CLI Scanner

### Escaneo básico

```bash
python3 cors_scanner.py -u https://api.target.com/endpoint
```

### Lista de URLs

```bash
python3 cors_scanner.py -L targets.txt -o results.json
```

### Con autenticación

```bash
python3 cors_scanner.py -u https://api.target.com/data \
  --auth-header "Authorization: Bearer TOKEN" \
  -v
```

### Escaneo POST

```bash
python3 cors_scanner.py -u https://api.target.com/update \
  -m POST \
  --body '{"test":"cors"}' \
  -o results.json
```

---

## ⚙️ Opciones CLI

| Flag              | Descripción                                |
|-------------------|-----------------------------------------|
| `-u, --url`       | URL objetivo                            |
| `-L, --list`      | Archivo con lista de URLs               |
| `-m, --method`    | Método HTTP (default: GET)              |
| `--auth-header`   | Header de autenticación                 |
| `--body`          | Body para POST/PUT                      |
| `-T, --threads`   | Número de threads (default: 10)         |
| `-t, --timeout`   | Timeout en segundos (default: 10)       |
| `-o, --json-output` | Guardar resultados en JSON            |
| `-v, --verbose`   | Modo verbose                            |

---

## 🎯 Vulnerabilidades Detectadas

### Critical
- **Credentials + Origin Reflection**: Permite exfiltrar datos sensibles
  - `Access-Control-Allow-Origin: https://evil.com`
  - `Access-Control-Allow-Credentials: true`

### High
- **Dynamic Origin Reflection**: Origin del atacante reflejado
- **Null Origin Accepted**: `Access-Control-Allow-Origin: null`
- **File Protocol Accepted**: `file://` permitido
- **Data URI Accepted**: `data:text/html` permitido

### Medium
- **Wildcard Misconfiguration**: `Access-Control-Allow-Origin: *`

### Patterns Tested

```
✓ https://evil.com (External attacker)
✓ null (Null origin bypass)
✓ https://target.com.attacker.com (Subdomain prefix)
✓ https://attacker.target.com (Subdomain injection)
✓ https://sub.target.com (Subdomain trust)
✓ http://target.com (Protocol downgrade)
✓ file:// (File protocol)
✓ data:text/html (Data URI)
✓ http://localhost (Localhost)
✓ https://target.com:8080 (Port variation)
```

---

## 📊 Formato JSON Output (CLI)

```json
{
  "scanner_version": "2.0",
  "targets_scanned": 10,
  "vulnerable_urls": 3,
  "total_vulnerabilities": 5,
  "severity_summary": {
    "critical": 1,
    "high": 3,
    "medium": 1,
    "low": 0
  },
  "findings": {
    "https://api.target.com/endpoint": [
      {
        "url": "https://api.target.com/endpoint",
        "origin": "https://evil.com",
        "method": "GET",
        "status_code": 200,
        "acao_header": "https://evil.com",
        "acac_header": "true",
        "vulnerabilities": [
          "Dynamic origin reflection",
          "Credentials + Origin reflection (CRITICAL)"
        ],
        "severity": "critical",
        "timestamp": 1709577600.123
      }
    ]
  }
}
```

---

## 🎨 Capturas de Pantalla

### Toolkit HTML
- UI moderna con dark theme
- Detección automática de vulnerabilidades
- Progress bars para escaneos masivos
- Export y copy to clipboard

### CLI Scanner
```
╭────────────────────────────────────────────╮
│  cors-scanner v2.0 - CORS Misconfiguration │
╰────────────────────────────────────────────╯

[+] Objetivos cargados: 15
Escaneando: 100%|████████████████| 15/15 [00:12<00:00,  1.21url/s]

[!] VULNERABLE: https://api.target.com/data with origin https://evil.com
    - Dynamic origin reflection
    - Credentials + Origin reflection (CRITICAL)

============================================================
[+] Escaneo completado
    Objetivos analizados: 15
    URLs vulnerables: 3
    Vulnerabilidades totales: 5

    Por severidad:
      - Critical: 1
      - High: 3
      - Medium: 1
```

---

## 📚 Casos de Uso

### Bug Bounty
```bash
# Escaneo de subdominios
cat subdomains.txt | while read domain; do
  python3 cors_scanner.py -u "$domain/api/endpoint" -o "cors_$domain.json"
done
```

### Pentesting
```bash
# Escaneo con autenticación
python3 cors_scanner.py -L targets.txt \
  --auth-header "Authorization: Bearer TOKEN" \
  --verbose
```

### CI/CD Security Testing
```bash
# Verificación automatizada
python3 cors_scanner.py -u https://staging.app.com/api \
  -o cors_check.json
```

---

## ⚠️ Limitaciones

- No soporta JavaScript rendering (pruebas estáticas)
- Requiere que el endpoint responda a CORS preflight
- No bypasea WAFs
- Detección basada en headers (no ejecuta exploits)

---

## 📖 Referencias

- [OWASP CORS Guide](https://owasp.org/www-community/attacks/CORS_OriginHeaderScrutiny)
- [PortSwigger CORS Vulnerabilities](https://portswigger.net/web-security/cors)
- [MDN CORS Documentation](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS)

---

## 📋 Uso Ético

Utiliza esta herramienta únicamente en:
- ✅ Sistemas propios
- ✅ Entornos autorizados
- ✅ Programas de bug bounty con scope definido

**El uso no autorizado es ilegal.**

---

## 📜 Licencia

MIT License
