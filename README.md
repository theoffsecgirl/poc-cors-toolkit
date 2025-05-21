# 🧪 PoC CORS Toolkit — Full Suite

Este proyecto es una herramienta completa en HTML puro para auditar configuraciones de CORS (Cross-Origin Resource Sharing) en aplicaciones web. Fue diseñada pensando en bug bounty hunters, pentesters y desarrolladores que quieran validar políticas CORS y detectar vulnerabilidades relacionadas como:

- Access-Control-Allow-Origin: *
- Reflejo dinámico de O
rigin
- CORS combinado con redirecciones (SSRF/CORS bypass)
- Permisos indebidos de `Authorization`, `Content-Type`, etc.

## 🚀 Características

- Soporte para GET y POST
- Inserción de `Origin` malicioso configurable
- Cabecera `Authorization` opcional
- Body personalizable para POST
- Detección de redirección HTTP (`302`, `301`, etc.)
- Impresión detallada de headers, estado, URL final y contenido de la respuesta
- Carga masiva de URLs y pruebas secuenciales
- Exportador de resultados en TXT
- Completamente en HTML + JS, ejecutable localmente (`file://`)

## 📦 Uso

1. Clona el repositorio:
```bash
git clone https://github.com/theoffsecgirl/poc-cors-toolkit.git
cd poc-cors-toolkit
```

2. Abre el archivo en tu navegador:
```bash
firefox poc_cors_toolkit.html
```

3. Ajusta los parámetros y lanza pruebas.

## ✍️ Ejemplo de uso

- Probar si un subdominio refleja el Origin:
```
URL objetivo: https://sub.example.com
Payload Origin: https://evil.com
```

- Detectar redirección CORS:
```
URL objetivo: https://example.com/redirect?to=https://evil.com
```

## 📜 Licencia

MIT — Libre para usar, modificar y distribuir. Credita si te sirvió 🙌

---

Hecho con 💚 por TheOffSecGirl
