from fastapi import FastAPI
from datetime import datetime


#creamos la instancia de la aplicación FastAPI
app = FastAPI()

@app.get("/hora-actual")
def obtener_hora():
    ahora = datetime.now()
    return {
        "fecha": ahora.strftime("%Y-%m-%d"),
        "hora": ahora.strftime("%H:%M:%S")
    }