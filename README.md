# Taller 6 — Prompt, contexto y mini-aplicación

Tema asignado: conversor de unidades (primer apellido: Fajardo).

## Languages

- Python — FastAPI y lógica de conversiones
- HTML — plantilla de la interfaz
- JavaScript — interacción del conversor
- CSS — diseño visual adaptable

## Descargar

[Descargar el proyecto completo en ZIP](https://github.com/miguelhacky/Mini-aplicaci-n/archive/refs/heads/main.zip)

## Actividades

1. **Preparación:** carpetas aisladas `mini-app-a` y `mini-app-b`.
2. **Versión A:** mini-aplicación creada desde un prompt de una línea; línea base con 5/8 pruebas de aceptación.
3. **Versión B:** prompt estructurado, `AGENTS.md`, contrato y aplicación organizada; 8/8 pruebas de aceptación.
4. **Comparación:** resultados y conclusión en `comparacion.md`.
5. **Mejora:** endpoint `/api/unidades`, interfaz dinámica y `tests/test_mejora.py`.
6. **Plantilla y registro:** `prompts/plantilla.md` y `prompts/semana-2-mini-app.md`.
7. **Lectura crítica:** ocho dudas con supuestos y justificación en `specs/dudas-encargo.md`.

## Ejecución de B

```powershell
python -m pytest -v
ruff check .
uvicorn app.main:app --reload
```
