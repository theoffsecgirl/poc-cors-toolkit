<div align="center">

# poc-cors-toolkit

**Toolkit HTML para auditar configuraciones CORS en aplicaciones web**

![Language](https://img.shields.io/badge/HTML-tool-9E4AFF?style=flat-square&logo=html5&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-9E4AFF?style=flat-square)
![Category](https://img.shields.io/badge/Category-Bug%20Bounty%20%7C%20PoC-111111?style=flat-square)

*by [theoffsecgirl](https://github.com/theoffsecgirl)*

</div>

---

## ¿Qué hace?

Herramienta standalone en HTML para probar políticas CORS desde el navegador: inserción de `Origin` personalizado, detección de reflejos dinámicos, validación de métodos permitidos, análisis de cabeceras de seguridad y comportamientos de redirección.

No requiere instalación ni servidor. Abre el archivo en el navegador y listo.

---

## Casos de uso

- Verificar si el servidor refleja cualquier `Origin` sin restricciones
- Comprobar si `Access-Control-Allow-Credentials: true` está habilitado junto a origen dinámico
- Validar qué métodos HTTP acepta el endpoint (GET, POST, OPTIONS)
- Detectar cabeceras de seguridad ausentes o mal configuradas
- Pruebas masivas con lista de endpoints

---

## Uso

```bash
git clone https://github.com/theoffsecgirl/poc-cors-toolkit
cd poc-cors-toolkit
firefox cors_toolkit.html
# o
open cors_toolkit.html   # macOS
```

Sin dependencias externas. No necesita Python, Node ni servidor local.

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

## CORS misconfiguration: ¿qué busca?

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
