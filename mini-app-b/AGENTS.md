# AGENTS.md
## Proyecto
Mini-aplicación de práctica: Conversor de unidades. Datos ficticios en memoria, sin base de datos.
## Stack
- Python 3.14, FastAPI y plantillas Jinja2
- pytest con TestClient, Ruff
## Comandos
- Instalar: `pip install -r requirements.txt`
- Ejecutar: `uvicorn app.main:app --reload`
- Pruebas: `python -m pytest -v`
- Estilo: `ruff check .`
## Estructura
- `app/main.py`: aplicación y rutas
- `app/servicios.py`: lógica de conversión
- `app/templates/index.html`: interfaz
- `tests/test_aceptacion.py`: contrato; no se modifica
## Qué no hacer
- No modificar ni borrar `tests/test_aceptacion.py`.
- No instalar dependencias fuera de `requirements.txt`.
- No usar base de datos ni archivos para guardar datos.
- No hacer commit ni push.
