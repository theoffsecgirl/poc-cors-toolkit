# Changelog

All notable changes to **corskit** are documented here.

---

## [1.1.0] – 2026-03-24

### Added
- `analyzeResponse()`: deteccion automatica de misconfigurations CORS con severidad (critical / high / info).
- `renderFindings()`: visualizacion highlight por severidad con color coding.
- Boton **Auto-scan origins**: prueba todos los origins generados de una vez y consolida findings.
- Origins adicionales: tld wildcard, bypass chars (`%60`, `..`), `data:text/html`, `file://`.
- Boton **Limpiar** para resetear output y findings.
- Nombre exportacion: `corskit_{timestamp}.txt`.

### Changed
- Repo renombrado: `poc-cors-toolkit` → `corskit`.
- UI reorganizada en grid 2 columnas para URL y metodo.
- Subtitulo con enlace a theoffsecgirl.com.

### Fixed
- Origins generados ahora respetan el protocolo del objetivo (http vs https).

---

## [1.0.0] – 2025-05-21

### Added
- Version inicial: prueba individual, lista de URLs, exportacion TXT.
