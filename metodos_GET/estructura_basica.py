"""
El método GET sirve para OBTENER (traer) datos.    
"""

# Importamos FastAPI para crear nuestra aplicación
from fastapi import FastAPI

# Creamos una instancia de nuestra aplicación FastAPI
# Esta instancia debe crearse una sola vez al inicio del archivo
app = FastAPI()

# Creamos la ruta raíz ("/")
# El decorador @app.get("/") le dice a FastAPI que cuando alguien visite la ruta raíz ("/"), tiene que ejecutar la función leer_raiz

@app.get("/")
def leer_raiz():
    return {"mensaje": "¡Hola, desde la ruta raíz!"}

