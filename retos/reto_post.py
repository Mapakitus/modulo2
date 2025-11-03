"""
Crea una API con FastAPI que permita crear libros mediante un endpoint POST.

Debes implementar:

Un modelo Pydantic llamado Libro con los siguientes campos:
titulo: string obligatorio
autor: string obligatorio
paginas: entero obligatorio
Un endpoint POST en la ruta /libros que:
Reciba un objeto Libro en el request body
Devuelva una respuesta JSON con:
Un mensaje de confirmación
Los datos del libro recibido
Para empezar, importa FastAPI y BaseModel de pydantic, crea la instancia de la aplicación, define el modelo y luego implementa el endpoint POST. El endpoint debe ser una función asíncrona que reciba el modelo como parámetro y retorne un diccionario con la respuesta.

Ejemplo del JSON que debe enviarse al endpoint:

{
  "titulo": "El Quijote",
  "autor": "Miguel de Cervantes",
  "paginas": 863
}    
"""

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Define aquí el modelo Libro
class Libro(BaseModel):
    titulo: str
    autor: str
    paginas: int

# Define aquí el endpoint POST
@app.post("/libros")
async def crear_libro(libro: Libro):
    return {
        "mensaje": f"Libro '{libro.titulo}' creado correctamente",
        "datos": {
            "titulo": libro.titulo,
            "autor": libro.autor,
            "paginas": libro.paginas
        }
    }   