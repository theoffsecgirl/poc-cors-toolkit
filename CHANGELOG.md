# Changelog

All notable changes to **corskit** are documented here.

---

## [1.3.0] – 2026-08-21

### Added
- `updateOrigins()`: 6 origins nuevos generados automaticamente, cubriendo bypasses reales citados en writeups de bug bounty:
  - Bypass de regex con punto sin escapar (`api.example.com` → `apiXexample.com`), el bypass de CORS mas citado (James Kettle / PortSwigger) y hasta ahora no cubierto.
  - Variante case-sensitivity del host (`Example.COM`).
  - Puertos no estandar `:4443` y `:8443` sobre el mismo host.
  - Downgrade de esquema `https` → `http` sobre el mismo host.
- Cruce automatico preflight-bloqueado × request simple: cuando `analyzePreflightResponse()` detecta un preflight rechazado (status 0/403/405), `testPreflight()` y `testPreflightAutoAll()` disparan un `doFetch()` de confirmacion contra el mismo `url`+`origin`. Si el handler principal responde igualmente con CORS mal configurado, se añade un finding `[CRUZADO] Preflight bloqueado pero handler principal vulnerable` (`critical`/`high` segun lo encontrado).
- `runPool()`: helper reutilizable de pool de concurrencia (limite `CONCURRENCY_LIMIT = 3`) usado por `testAutoAll()`, `testMultiple()` y `testPreflightAutoAll()`.

### Changed
- `testAutoAll()`, `testMultiple()` y `testPreflightAutoAll()` ahora ejecutan sus requests en paralelo (hasta 3 simultaneos via `runPool()`) en vez de secuencial con `for...await`, reduciendo la latencia total del auto-scan sin llegar a paralelismo total (evita parecer fuerza bruta / disparar WAFs).

### Fixed
- Deduplicacion de findings inconsistente entre auto-scans: `testAutoAll()` deduplicaba solo por `f.title`, colapsando hallazgos legitimos con el mismo titulo pero distinto `detail` (p. ej. la misma misconfiguration detectada en origins distintos). Ahora las tres funciones de auto-scan deduplican por `f.title + f.detail`, igual que ya hacian `testMultiple()` y `testPreflightAutoAll()`.

---

## [1.2.0] – 2026-03-25

### Added
- `Preflight OPTIONS` test: botón dedicado que lanza un `OPTIONS` real con `Access-Control-Request-Method` y `Access-Control-Request-Headers` configurables.
- `Preflight auto-scan`: prueba todos los origins generados con el preflight OPTIONS de una vez.
- `analyzePreflightResponse()`: deteccion automatica de misconfiguraciones en preflight:
  - Origin reflejado en OPTIONS (con/sin credenciales)
  - Metodos peligrosos: `DELETE`, `PUT`, `PATCH`, `CONNECT`, `TRACE`
  - Headers sensibles permitidos: `Authorization`, `x-api-key`, `x-auth-token`, `cookie`, `x-csrf-token`
  - Wildcard en `Access-Control-Allow-Headers`
  - null origin aceptado en preflight
  - `Access-Control-Max-Age` excesivo
  - Preflight bloqueado (403/405) con aviso de misconfiguration oculta
- Seccion visual separada `Preflight Findings` con badge `OPTIONS` en azul.
- `Timeout` configurable para el preflight (default: 8000ms).
- Metodos adicionales en selector: `PUT`, `DELETE`.
- Severidad `medium` para headers sensibles.

### Changed
- Selección de método ampliada a GET / POST / PUT / DELETE.
- Layout de opciones preflight en grid 3 columnas.
- Version bump a `1.2.0` en el subtitulo.

---

## [1.1.0] – 2026-03-24

### Added
- `analyzeResponse()`: deteccion automatica de misconfigurations CORS con severidad.
- `renderFindings()`: visualizacion highlight por severidad.
- Boton Auto-scan origins.
- Origins adicionales: tld wildcard, bypass chars, `data:text/html`, `file://`.
- Boton Limpiar y exportacion `corskit_{timestamp}.txt`.

### Changed
- Repo renombrado: `poc-cors-toolkit` → `corskit`.

---

## [1.0.0] – 2025-05-21

### Added
- Version inicial: prueba individual, lista de URLs, exportacion TXT.
