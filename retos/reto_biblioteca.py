"""
Crea una aplicación FastAPI con dos endpoints GET específicos:

Un endpoint en la ruta /libros que devuelva una respuesta JSON con una lista de 3 libros. Cada libro debe ser simplemente un string con el título.

Un endpoint en la ruta /biblioteca que devuelva información básica sobre la biblioteca en formato JSON, incluyendo el nombre de la biblioteca, la cantidad total de libros y si está abierta.

Para empezar:

Importa FastAPI
Crea la instancia de la aplicación con app = FastAPI()
Define cada endpoint usando el decorador @app.get() seguido de la función correspondiente
Cada función debe devolver un diccionario de Python (FastAPI lo convertirá automáticamente a JSON)
Para el endpoint de biblioteca, incluye las claves: "nombre", "total_libros" (número), y "abierta" (booleano).    
 """

from fastapi import FastAPI

# Crear la instancia de la aplicación
app = FastAPI()

# Escribe aquí tu código para los endpoints GET

# ruta de libros
@app.get("/libros")
def obtener_libros():
# devolvemos una lista de libros
    return {"productos": ["Los pilares de la tierra", "Ubik", "El principito"]}

#ruta de biblioteca
@app.get("/biblioteca")
def leer_biblioteca():
# devolvemos información de la biblioteca
    return {"nombre": "Biblioteca de Amnuminas", "total_libros": 3, "abierta": True}