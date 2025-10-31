from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Modelo Pydantic para la respuesta
class Producto(BaseModel):
    id: int
    nombre: str
    precio: float
    disponible: bool = True
    
# Base de datos simulada
    
productos_db : List[Producto] = [
    Producto(id=1, nombre="Portátil", precio=999.99, disponible=True),
    Producto(id=2, nombre="Ratón", precio=25.50, disponible=True),
    Producto(id=3, nombre="Teclado", precio=49.99, disponible=False)
]

#método GET para obtener la lista de objetos Producto
@app.get("/productos", response_model=List[Producto])
def listar_productos():
    return productos_db

# método GET para obtener un producto por su id
@app.get("/productos/{producto_id}", response_model=Producto)
def obtener_producto(producto_id: int):
    #recoorrer la base de datos simulada para encontrar el producto
    for p in productos_db:
        #si el id coincide, devolver el producto pydantic directamente
        if p.id == producto_id:
            return p
    raise HTTPException(status_code=404, detail="Producto no encontrado")

# método POST para agregar un nuevo producto y que devuelva el 201 Created
@app.post("/productos", response_model=Producto, status_code=201)
def crear_producto(producto: Producto):
    #añadir el nuevo producto a la base de datos simulada
    productos_db.append(producto)
    return producto


