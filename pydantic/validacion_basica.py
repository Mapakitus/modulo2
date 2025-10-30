from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

# Crear la instancia de la aplicación

app = FastAPI()

# modelo básico
class Usuario(BaseModel):
    nombre: str
    email: str
    edad: int
    activo: bool


#modelo con campos opcionales y valores por defecto
class Producto(BaseModel):
    nombre: str
    precio: float
    descripcion: Optional[str] = None
    disponible: bool = True

@app.post("/usuarios")
def crear_usuario(usuario: Usuario):
    return {
        "mensaje": f"Usuario {usuario.nombre} creado correctamente"      
    }

@app.post("/productos")
def crear_producto(producto: Producto):
    return {
        "producto_creado": producto.nombre,
        "precio": producto.precio,
        "descripcion": producto.descripcion,
        "disponible": producto.disponible
    }


    
    




