"""
Crea una aplicación FastAPI con un endpoint GET que busque un libro por su ID. Si el libro no existe, debe lanzar una HTTPException con código 404 y el mensaje "Libro no encontrado".

Instrucciones paso a paso:

Importa FastAPI y HTTPException
Crea la instancia de la aplicación FastAPI
Define una lista de libros con al menos 2 libros, cada uno con 'id', 'titulo' y 'autor'
Crea un endpoint GET en la ruta '/libros/{libro_id}' que reciba libro_id como parámetro de tipo int
Busca el libro en la lista comparando el ID
Si encuentras el libro, devuélvelo
Si no lo encuentras, lanza HTTPException con status_code=404 y detail="Libro no encontrado"
Ejemplo de datos para la lista:

Libro 1: id=1, titulo="El Quijote", autor="Cervantes"
Libro 2: id=2, titulo="Cien años de soledad", autor="García Márquez"
"""

from fastapi import FastAPI, HTTPException

# Crear la aplicación FastAPI
app = FastAPI()

# Lista de libros
libros = [
    # Agrega aquí los libros con id, titulo y autor
    {"id": 1, "titulo": "El Quijote", "autor": "Cervantes"},
    {"id": 2, "titulo": "Cien años de soledad", "autor": "García Márquez"},
    {"id": 3, "titulo": "1984", "autor": "George Orwell"}
]

# Crear el endpoint GET
@app.get("/libros/{libro_id}")
def obtener_libro(libro_id: int):
    # Buscar el libro por ID
    for libro in libros:
        if libro["id"] == libro_id:
            return libro
    # Si no se encuentra, lanzar HTTPException
    raise HTTPException(status_code=404, detail="Libro no encontrado")