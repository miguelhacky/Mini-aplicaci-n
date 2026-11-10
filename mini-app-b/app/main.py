from pathlib import Path

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from .servicios import UNIDADES, convertir

app = FastAPI(title="Conversor de unidades")
templates = Jinja2Templates(directory=str(Path(__file__).parent / "templates"))

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(request=request, name="index.html", context={"unidades": UNIDADES})

@app.get("/api/unidades")
def unidades():
    return UNIDADES

@app.get("/api/convertir")
def convertir_api(tipo: str, valor: float, de: str, a: str):
    try:
        resultado = convertir(tipo, valor, de, a)
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error)) from error
    return {"resultado": round(resultado, 4)}
