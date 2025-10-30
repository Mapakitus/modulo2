"""
Si no capturamos errores, entonces la aplicación devuelve error 500 Internal Server Error.

Consejo: se puede empezar haciendo las funcionalidades y cuando estén programadas, ya se 
introduce la gestión de errrores: try except.

"""

from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/")
def leer_raiz():
    try:
        resultado = 10 / 0
    except:
        raise HTTPException(status_code=404, detail="No existe lo que buscas")
    return {"resultado": resultado}