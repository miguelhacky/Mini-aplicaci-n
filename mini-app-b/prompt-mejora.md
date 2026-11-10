## Rol
Actúa como desarrollador backend con experiencia en FastAPI y pruebas con pytest.

## Objetivo
Agrega la mejora de unidades a la aplicación existente: crea GET /api/unidades para devolver los tipos de medida y sus unidades disponibles, y usa esa información para llenar los selectores de la página.

## Contexto
Lee AGENTS.md, app/main.py, app/servicios.py, app/templates/index.html y tests/test_aceptacion.py. La aplicación ya convierte temperatura, longitud y masa.

## Restricciones
- No modifiques ni borres tests/test_aceptacion.py.
- No uses base de datos ni archivos para guardar datos.
- Mantén la separación entre rutas en app/main.py y lógica en app/servicios.py.
- Agrega tests/test_mejora.py para comprobar la nueva respuesta.
- Conserva el diseño actual de la página.

## Formato de salida
Primero muestra un plan con las rutas completas de los archivos que modificarás. Espera mi aprobación antes de escribir código. Después resume el diff.

## Ejemplo
GET /api/unidades devuelve:

{"temperatura": ["C", "F", "K"], "longitud": ["mm", "cm", "m", "km"], "masa": ["g", "kg", "lb"]}

## Criterio de éxito
python -m pytest -v pasa todas las pruebas y ruff check . no reporta errores. Si una prueba falla, explica la causa antes de cambiar otra cosa.
