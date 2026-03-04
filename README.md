# poc-cors-toolkit v2.0

Suite avanzada para auditoría de configuraciones **CORS (Cross-Origin Resource Sharing)** en aplicaciones web modernas.

---

## 🚀 Novedades v2.0 (2026)

### Mejoras Técnicas
- ✅ **Detección automática de vulnerabilidades** (6 tipos)
- ✅ **Sistema de severidad** (high/medium/low)
- ✅ **Testing masivo** con múltiples URLs y origins
- ✅ **Custom headers** con soporte JSON
- ✅ **Métodos HTTP avanzados** (PUT, PATCH, DELETE, OPTIONS)
- ✅ **JSON reporting** estructurado
- ✅ **Stats dashboard** en tiempo real
- ✅ **Enhanced origin payloads** (15+)

### Vulnerabilidades Detectadas

1. **REFLECTED_ORIGIN** (High)
   - Origin dinámico reflejado en ACAO
   - Permite bypass con cualquier dominio atacante

2. **WILDCARD_WITH_CREDENTIALS** (High)
   - ACAO: * con credentials habilitadas
   - Configuración inválida y peligrosa

3. **PRE_DOMAIN_WILDCARD** (High)
   - Wildcard en subdominio (ej: `https://*.example.com`)
   - Permite ataques desde subdominios controlados

4. **NULL_ORIGIN_ACCEPTED** (Medium)
   - Origin `null` aceptado
   - Explotable via sandbox iframe

5. **INSECURE_PROTOCOL** (Medium)
   - Protocolos inseguros aceptados (file://, data:)
   - Bypass de restricciones de origen

6. **MISSING_HEADERS** (Low)
   - Headers de seguridad ausentes
   - Configuración incompleta

---

## 📦 Instalación

```bash
git clone https://github.com/theoffsecgirl/poc-cors-toolkit
cd poc-cors-toolkit
```

Abrir en navegador:

```bash
firefox cors-toolkit.html
# o
open cors-toolkit.html
```

**No requiere dependencias ni servidor.** Funciona 100% client-side.

---

## 🔥 Uso Básico

### Prueba Individual

1. Ingresar URL objetivo: `https://api.example.com/data`
2. Seleccionar origin de prueba: `https://evil.com`
3. Click en **"Prueba Individual"**
4. Revisar output para vulnerabilidades detectadas

### Testing Masivo

1. Agregar múltiples URLs en "Lista de URLs":
   ```
   https://api.example.com/users
   https://api.example.com/admin
   https://sub.example.com/api
   ```
2. Click en **"Testing Masivo"**
3. Esperar completar todas las pruebas
4. Exportar resultados en TXT o JSON

### Test All Origins

1. Configurar URL objetivo
2. Click en **"Test All Origins"**
3. Prueba automática con 15+ origins diferentes
4. Revisión completa de misconfigurations

---

## ⚙️ Funcionalidades

### Origin Payloads (15+)

**Estáticos:**
- `https://evil.com`
- `https://attacker.com`
- `null`
- `file://`
- `data:text/html,<script>alert(1)</script>`

**Dinámicos (auto-generados):**
- `https://[target].attacker.com`
- `https://evil.[target]`
- `https://sub.[target]`
- `https://[target].evil.com`
- `https://[target]:8080`

### Métodos HTTP
- GET, POST, PUT, DELETE, PATCH, OPTIONS

### Custom Headers
Soporte para headers personalizados en formato JSON:
```json
{
  "X-API-Key": "abc123",
  "X-Custom-Header": "value",
  "X-Tenant-ID": "tenant-001"
}
```

### Authorization
Soporte para tokens Bearer, API keys, cookies, etc:
```
Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

---

## 📊 Ejemplo de Salida

### Output de Vulnerabilidad

```
╭────────────────────────────────────────────────────────────╮
│ URL: https://api.example.com/data
│ Origin: https://evil.com
│ Método: GET
│ Status: 200
╰────────────────────────────────────────────────────────────╯

Response Headers:
  access-control-allow-origin: https://evil.com
  access-control-allow-credentials: true
  content-type: application/json

🚨 VULNERABILIDADES DETECTADAS:

[HIGH] REFLECTED_ORIGIN
    Origin https://evil.com reflejado dinámicamente en ACAO
    Evidence: Access-Control-Allow-Origin: https://evil.com

Body Preview:
{"user":"admin","role":"superuser",...}
```

### JSON Report

```json
{
  "generated_at": "2026-03-04T17:40:00.123Z",
  "tool": "CORS Toolkit v2.0",
  "statistics": {
    "requests": 15,
    "vulns": 3,
    "errors": 0
  },
  "vulnerabilities": [
    {
      "url": "https://api.example.com/data",
      "origin": "https://evil.com",
      "vulns": [
        {
          "severity": "high",
          "type": "REFLECTED_ORIGIN",
          "description": "Origin https://evil.com reflejado dinámicamente en ACAO",
          "evidence": "Access-Control-Allow-Origin: https://evil.com"
        }
      ]
    }
  ],
  "results": []
}
```

---

## 🎯 Casos de Uso

### Bug Bounty
```
1. Probar múltiples endpoints del scope
2. Usar "Test All Origins" para cobertura completa
3. Exportar JSON para reporting
4. Priorizar vulnerabilidades High severity
```

### Pentesting
```
1. Configurar Authorization header con token de sesión
2. Testing de endpoints autenticados
3. Custom headers para APIs complejas
4. Validación de mitigaciones
```

### Desarrollo Seguro
```
1. Testing en staging antes de producción
2. Verificación de configuración CORS correcta
3. Validación de headers de seguridad
4. CI/CD integration con JSON output
```

---

## ⚠️ Limitaciones

- Requiere que el navegador permita peticiones CORS (por diseño)
- No puede hacer bypass de CORS del navegador (testing legítimo)
- OPTIONS preflight requests manejadas automáticamente por el navegador
- Credenciales del navegador incluidas automáticamente si están disponibles

---

## 🔬 Roadmap

- [ ] Detección de CORS bypass techniques
- [ ] Automatic PoC generation
- [ ] Integration con Burp Suite
- [ ] Batch testing desde archivo
- [ ] Advanced reporting con gráficas
- [ ] Browser extension version

---

## 📖 Uso Ético

Utiliza esta herramienta únicamente en:
- ✅ Aplicaciones propias
- ✅ Entornos autorizados
- ✅ Programas de bug bounty con scope definido

**El uso no autorizado es ilegal.**

---

## 📜 Licencia

MIT License
