## Rol
Actúa como desarrollador backend con experiencia en FastAPI y pruebas con pytest.

## Objetivo
Agrega el endpoint GET /api/unidades para devolver los tipos de medida y sus unidades disponibles.

## Contexto
Lee AGENTS.md, app/main.py, app/servicios.py y tests/test_aceptacion.py.

## Restricciones
- No modifiques tests/test_aceptacion.py.
- No uses base de datos.
- Mantén la estructura actual del proyecto.
- Agrega una prueba en tests/test_mejora.py.
- La página debe usar el endpoint para cargar las unidades.

## Formato de salida
Primero muestra un plan con los archivos que modificarás. Espera mi aprobación antes de escribir código.

## Ejemplo
GET /api/unidades devuelve:

{
  "temperatura": ["C", "F", "K"],
  "longitud": ["mm", "cm", "m", "km"],
  "masa": ["g", "kg", "lb"]
}

## Criterio de éxito
python -m pytest -v pasa todas las pruebas y ruff check . no reporta errores.