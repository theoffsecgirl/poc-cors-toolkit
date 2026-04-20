# corskit

Herramienta de evaluación de CORS para uso manual en navegador.

> 🇬🇧 [English version](README.md)

---

## ¿Qué hace?

Herramienta web (HTML + JavaScript puro, sin dependencias) para ayudar a evaluar el comportamiento CORS de endpoints. Permite probar un endpoint, lanzar un barrido de origins, inspeccionar preflight y revisar findings heurísticos.

Importante: es una **herramienta de apoyo**, no un verificador definitivo de vulnerabilidades.

---

## Para qué sirve realmente

- Triage rápido de CORS en un endpoint
- Comparar comportamiento entre distintos origins
- Analizar respuestas preflight `OPTIONS`
- Inspeccionar headers en pruebas manuales
- Construir PoCs una vez identificado el problema

---

## Limitaciones importantes

- El navegador limita lo que puede testearse desde JavaScript
- La cabecera `Origin` no es totalmente controlable
- La severidad (`critical`, `high`, `info`) es heurística
- Un resultado positivo requiere validación manual real

---

## Funcionalidades

- Test manual por origin
- Auto-scan de múltiples origins
- Pruebas preflight `OPTIONS`
- Clasificación heurística
- Generación de origins (subdominios, bypass, `null`, etc.)
- Métodos configurables
- Exportación en `.txt`
- Sin dependencias externas

---

## Uso

```bash
git clone https://github.com/theoffsecgirl/corskit.git
cd corskit
open cors_toolkit.html
```

O con servidor local:

```bash
python3 -m http.server 8080
```

Nota: esto no elimina las restricciones CORS del navegador.

---

## Flujo recomendado

1. Detectar sospecha de CORS
2. Usar corskit para comparar origins
3. Analizar headers y preflight
4. Validar manualmente antes de reportar

---

## Uso ético

Solo para entornos autorizados.

---

## Licencia

MIT
