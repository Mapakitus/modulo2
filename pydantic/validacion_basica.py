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

#modelo con campos opcionales y valores por defecto
class Producto(BaseModel):
    nombre: str
    precio: float
    descripcion: Optional[str] = None
    disponible: bool = True



    
    




