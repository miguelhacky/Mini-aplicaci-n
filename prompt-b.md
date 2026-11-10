## Rol
Actúa como desarrollador backend con experiencia en FastAPI, Jinja2 y pruebas con pytest.
## Objetivo
Construir la mini-aplicación web Conversor de unidades con estos requisitos:
1. GET / muestra un formulario para elegir el tipo de medida, el valor y las unidades de origen y de destino, y muestra el resultado sin recargar la página.
2. GET /api/convertir recibe tipo, valor, de y a, y devuelve {"resultado": número}, redondeado a 4 decimales.
3. Tipos y unidades: temperatura (C, F, K), longitud (mm, cm, m, km) y masa (g, kg, lb).
4. Si el tipo o una unidad no son válidos, o si las unidades no corresponden al tipo, responde 400 con un mensaje en detail.
## Contexto
Lee AGENTS.md. El contrato está en tests/test_aceptacion.py: rutas, nombres de campos y estados deben coincidir.
## Restricciones
- Usa solo requirements.txt.
- Define rutas en app/main.py y lógica en app/servicios.py, sin importar FastAPI en servicios.
- No uses base de datos ni archivos para guardar datos.
- No modifiques tests/test_aceptacion.py.
- Usa HTML, CSS y JavaScript sin librerías externas.
## Formato de salida
Antes de escribir código, muestra el plan con las rutas completas y espera aprobación. Al terminar resume cada archivo.
## Ejemplo
GET /api/convertir?tipo=temperatura&valor=100&de=C&a=F devuelve {"resultado": 212.0}.
GET /api/convertir?tipo=masa&valor=1&de=kg&a=lb devuelve {"resultado": 2.2046}.
## Criterio de éxito
python -m pytest -v pasa todas las pruebas y ruff check . no reporta errores. Tras 3 intentos fallidos, detente y explica.
