<div align="center">

# corskit

**CORS misconfiguration tester — offensive web tool**

![Language](https://img.shields.io/badge/HTML%20%2F%20JS-Browser-9E4AFF?style=flat-square&logo=javascript&logoColor=white)
![Version](https://img.shields.io/badge/version-1.1.0-9E4AFF?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-9E4AFF?style=flat-square)
![Category](https://img.shields.io/badge/Category-Bug%20Bounty%20%7C%20Pentesting-111111?style=flat-square)

*by [theoffsecgirl](https://github.com/theoffsecgirl)*

> 🇪🇸 [Versión en español](README.es.md)

</div>

---

## What does it do?

Web tool (pure HTML + JavaScript, no dependencies) to detect CORS misconfigurations in web endpoints. Allows testing a single endpoint, running an automatic scan of pre-generated origins, and visualizing results with severity classification.

---

## Features

- Manual test per individual origin
- **Auto-scan**: tests all auto-generated origins at once
- Misconfiguration detection with severity: `critical` / `high` / `info`
- Generated origins: subdomains, wildcard TLD, bypass chars (`%60`, `..`), `null`, `data:`, `file://`
- Configurable method: `GET`, `POST`, `PUT`, `DELETE`, `OPTIONS`
- Export results as `corskit_{timestamp}.txt`
- No external dependencies — open directly in browser

---

## Usage

### Option 1 — Open directly

```bash
git clone https://github.com/theoffsecgirl/corskit.git
cd corskit
open cors_toolkit.html   # macOS
xdg-open cors_toolkit.html  # Linux
```

### Option 2 — Local server (avoids browser's own CORS restrictions)

```bash
python3 -m http.server 8080
# Open: http://localhost:8080/cors_toolkit.html
```

---

## Main file

`cors_toolkit.html` — single file, fully self-contained.

---

## Ethical use

For bug bounty, labs and authorized audits only.

---

## License

MIT · [theoffsecgirl](https://theoffsecgirl.com)
