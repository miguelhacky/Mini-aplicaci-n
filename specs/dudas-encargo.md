# Dudas del encargo

| Tipo | Duda | Supuesto adoptado | Justificación |
|---|---|---|---|
| funcional | ¿La conversión debe aceptar decimales? | Sí | Los valores físicos normalmente no son solo enteros. |
| funcional | ¿Se redondea el resultado? | A 4 decimales | El ejemplo fija una precisión concreta. |
| validación | ¿Qué ocurre con unidades mezcladas? | Responde 400 | No representan una conversión válida. |
| interfaz | ¿La página recarga al convertir? | No recarga | El requisito pide mostrar el resultado sin recargar. |
| datos | ¿Se persisten conversiones? | No | El encargo no solicita historial ni base de datos. |
| API | ¿El tipo distingue mayúsculas? | Usa los nombres exactos | El contrato enumera valores cerrados. |
| errores | ¿Dónde se informa el error? | En `detail` | Es el campo estándar de HTTPException en FastAPI. |
| mejora | ¿La mejora cambia el contrato inicial? | Agrega `/api/unidades` | La mejora describe un endpoint adicional. |
