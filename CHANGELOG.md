# Changelog

All notable changes to **corskit** are documented here.

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
