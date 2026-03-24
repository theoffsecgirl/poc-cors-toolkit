<div align="center">

# corskit

**Toolkit HTML para auditar configuraciones CORS en aplicaciones web**

![Language](https://img.shields.io/badge/HTML-tool-9E4AFF?style=flat-square&logo=html5&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-9E4AFF?style=flat-square)
![Category](https://img.shields.io/badge/Category-Bug%20Bounty%20%7C%20PoC-111111?style=flat-square)

*by [theoffsecgirl](https://github.com/theoffsecgirl)*

</div>

---

```text
┌──────────────────────────────────────────────────────┐
│                                                      │
│   ██████╗ ██████╗  ██████╗  ██████╗ ██████╗  │
│  ██╔════╝██╔══██╗██╔══██╗██╔════╝██╔══██╗ │
│  ██║     ██║  ██║██████╔╝█████╗  ██║  ██║ │
│  ██║     ██║  ██║██╔══██╗██╔══╝  ██║  ██║ │
│  ╚██████╗██████╔╝██║  ██║███████╗██████╔╝ │
│   ╚═════╝╚═════╝ ╚═╝  ╚═╝╚══════╝╚═════╝  │
│                                                      │
│  ██████╗ █████╗  ███████╗ ██████╗              │
│  ██╔════╝██╔══██╗ ██╔════╝██╔════╝              │
│  █████╗  ██║  ██║ █████╗  ██████╗               │
│  ██╔══╝  ██║  ██║ ██╔══╝  ╚════██╗              │
│  ██║     ╚█████╔╝ ███████╗██████╔╝              │
│  ╚═╝      ╚════╝  ╚══════╝╚═════╝               │
│                                                      │
│  CORS misconfiguration auditor  ·  by theoffsecgirl  │
└──────────────────────────────────────────────────────┘
```

---

## ¿Qué hace?

Herramienta standalone en HTML para probar políticas CORS desde el navegador. Sin instalación ni servidor: abre el archivo y listo.

---

## Casos de uso

- Verificar si el servidor refleja cualquier `Origin` sin restricciones
- Comprobar `Access-Control-Allow-Credentials: true` junto a origen dinámico
- Validar métodos HTTP permitidos (GET, POST, OPTIONS)
- Detectar cabeceras de seguridad ausentes o mal configuradas
- Pruebas masivas con lista de endpoints

---

## Uso

```bash
git clone https://github.com/theoffsecgirl/corskit
cd corskit
firefox cors_toolkit.html
# o
open cors_toolkit.html   # macOS
```

Sin dependencias. No necesita Python, Node ni servidor local.

---

## Funcionalidades

```text
[+] Inserción controlada de Origin personalizado
[+] Pruebas GET y POST
[+] Authorization opcional (Bearer token)
[+] Detección de reflejo dinámico del Origin
[+] Pruebas masivas por lista de endpoints
[+] Exportación de resultados
```

---

## Patrones CORS que detecta

| Patrón | Impacto |
|--------|---------|
| `Access-Control-Allow-Origin: *` + credenciales | Alto |
| Reflejo dinámico del Origin sin validación | Alto |
| `null` origin aceptado | Medio-Alto |
| Subdominio de atacante aceptado | Alto |
| Preflight con métodos peligrosos permitidos | Medio |

---

## Uso ético

Solo para bug bounty, laboratorios y auditorías autorizadas.

---

## Licencia

MIT · [theoffsecgirl](https://theoffsecgirl.com)
