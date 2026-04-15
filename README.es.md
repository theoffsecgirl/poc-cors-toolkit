<div align="center">

# corskit

**CORS misconfiguration tester — herramienta web ofensiva**

![Language](https://img.shields.io/badge/HTML%20%2F%20JS-Browser-9E4AFF?style=flat-square&logo=javascript&logoColor=white)
![Version](https://img.shields.io/badge/version-1.1.0-9E4AFF?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-9E4AFF?style=flat-square)
![Category](https://img.shields.io/badge/Category-Bug%20Bounty%20%7C%20Pentesting-111111?style=flat-square)

*by [theoffsecgirl](https://github.com/theoffsecgirl)*

> 🇬🇧 [English version](README.md)

</div>

---

## ¿Qué hace?

Herramienta web (HTML + JavaScript puro, sin dependencias) para detectar misconfigurations CORS en endpoints web. Permite testear un endpoint único, lanzar un escaneo automático de origins precalculados y visualizar los resultados con clasificación de severidad.

---

## Funcionalidades

- Test manual por origin individual
- **Auto-scan**: prueba todos los origins generados automáticamente de una vez
- Detección de misconfigurations con severidad: `critical` / `high` / `info`
- Origins generados: subdominios, wildcard tld, bypass chars (`%60`, `..`), `null`, `data:`, `file://`
- Método configurable: `GET`, `POST`, `PUT`, `DELETE`, `OPTIONS`
- Exportación de resultados como `corskit_{timestamp}.txt`
- Sin dependencias externas — abre directamente en el navegador

---

## Uso

### Opción 1 — Abrir directo

```bash
git clone https://github.com/theoffsecgirl/corskit.git
cd corskit
open cors_toolkit.html   # macOS
xdg-open cors_toolkit.html  # Linux
```

### Opción 2 — Servidor local (evita restricciones CORS del propio navegador)

```bash
python3 -m http.server 8080
# Abrir: http://localhost:8080/cors_toolkit.html
```

---

## Archivo principal

`cors_toolkit.html` — fichero único, todo autocontenido.

---

## Uso ético

Solo para bug bounty, laboratorios y auditorías autorizadas.

---

## Licencia

MIT · [theoffsecgirl](https://theoffsecgirl.com)
