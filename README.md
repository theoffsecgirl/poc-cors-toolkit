# corskit

CORS misconfiguration evaluator for manual testing in the browser.

> 🇪🇸 [Versión en español](README.es.md)

---

## What does it do?

Browser-based tool (pure HTML + JavaScript, no dependencies) to help evaluate CORS behavior on web endpoints. It lets you test one endpoint, run an automatic origin sweep, inspect preflight responses, and review heuristic findings.

Important: this is a **manual evaluation aid**, not a definitive vulnerability confirmer.

---

## What it is good for

- Quick CORS triage on a specific endpoint
- Comparing behavior across multiple candidate origins
- Inspecting preflight `OPTIONS` responses
- Reviewing raw response headers during manual validation
- Building PoCs after you already suspect a CORS issue

---

## Important limitations

- Browser behavior constrains what can be tested from client-side JavaScript
- The `Origin` header is not fully user-controlled in normal browser execution
- Heuristic severity (`critical`, `high`, `info`) is guidance, not proof of exploitability
- A positive result still requires manual validation in the real attack context

---

## Features

- Manual test per origin
- Auto-scan across generated origins
- Preflight `OPTIONS` testing
- Heuristic severity classification
- Generated origins: subdomains, wildcard-style variants, bypass chars, `null`, `data:`, `file://`
- Configurable method: `GET`, `POST`, `PUT`, `DELETE`, `OPTIONS`
- Export raw results as `corskit_{timestamp}.txt`
- No external dependencies — open directly in browser

---

## Usage

### Option 1 — Open directly

```bash
git clone https://github.com/theoffsecgirl/corskit.git
cd corskit
open cors_toolkit.html
```

### Option 2 — Local server

```bash
python3 -m http.server 8080
# Open: http://localhost:8080/cors_toolkit.html
```

Running it from a local server is often more practical, but it does **not** remove the browser's CORS model or magically grant full control over `Origin` handling.

---

## Main file

`cors_toolkit.html` — single self-contained file.

---

## Recommended workflow

1. Suspect a CORS issue on a target endpoint
2. Use corskit to compare multiple origins and inspect preflight responses
3. Review raw headers and identify whether behavior is reflected, wildcarded or credentialed
4. Validate manually with a real PoC before reporting

---

## Ethical use

For bug bounty, labs and authorized audits only.

---

## License

MIT
