#Ejecutar en la terminal uvicorn metodos_GET.prueba:app --reload

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}