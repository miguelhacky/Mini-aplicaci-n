from fastapi.testclient import TestClient

from app.main import app

cliente = TestClient(app)

def test_api_unidades_devuelve_tipos_y_unidades():
    assert cliente.get("/api/unidades").json() == {"temperatura": ["C", "F", "K"], "longitud": ["mm", "cm", "m", "km"], "masa": ["g", "kg", "lb"]}
