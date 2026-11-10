UNIDADES = {"temperatura": ["C", "F", "K"], "longitud": ["mm", "cm", "m", "km"], "masa": ["g", "kg", "lb"]}

def convertir(tipo: str, valor: float, de: str, a: str) -> float:
    if tipo not in UNIDADES or de not in UNIDADES[tipo] or a not in UNIDADES[tipo]:
        raise ValueError("tipo o unidad no válida")
    if tipo == "temperatura":
        celsius = {"C": valor, "F": (valor - 32) * 5 / 9, "K": valor - 273.15}[de]
        return {"C": celsius, "F": celsius * 9 / 5 + 32, "K": celsius + 273.15}[a]
    factores = {"longitud": {"mm": 0.001, "cm": 0.01, "m": 1, "km": 1000}, "masa": {"g": 1, "kg": 1000, "lb": 453.592}}[tipo]
    return valor * factores[de] / factores[a]
