from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import HTMLResponse

app = FastAPI(title="Conversor de unidades - Versión A")

@app.get("/", response_class=HTMLResponse)
def home() -> str:
    return """<html><body><h1>Conversor de unidades</h1><p>Usa /api/convertir.</p></body></html>"""

@app.get("/api/convertir")
def convertir(tipo: str, valor: float, de: str, a: str) -> dict[str, float]:
    if tipo == "temperatura":
        if de == "C" and a == "F":
            resultado = valor * 9 / 5 + 32
        elif de == "F" and a == "C":
            resultado = (valor - 32) * 5 / 9
        else:
            resultado = valor
    elif tipo == "longitud":
        factores = {"mm": 0.001, "cm": 0.01, "m": 1, "km": 1000}
        resultado = valor * factores.get(de, 1) / factores.get(a, 1)
    else:
        factores = {"g": 1, "kg": 1000, "lb": 453.592}
        resultado = valor * factores.get(de, 1) / factores.get(a, 1)
    return {"resultado": round(resultado, 4)}
