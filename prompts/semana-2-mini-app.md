# Registro de prompts
## Versión A
Haz una app web de conversión de unidades con FastAPI.
Resultado: línea base en `mini-app-a`; 5 de 8 pruebas pasan y 3 fallan.

## Versión B
Ver [prompt-b.md]. Resultado: contrato y mejora pasan; Ruff queda limpio.

## Mejora
Agrega un endpoint GET /api/unidades que devuelva los tipos con sus unidades y usa ese endpoint en la página para llenar las listas según el tipo elegido.
Resultado: `tests/test_mejora.py` pasa.
