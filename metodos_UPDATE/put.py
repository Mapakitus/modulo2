from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

usuarios_db = [
    {"id": 1, "nombre": "Grajilla", "email": "grajilla@aves.com"},
    {"id": 2, "nombre": "Rabilargo", "email": "rabilargo@aves.com"}
]

class Usuario(BaseModel):
    nombre: str
    email: str
    edad: int
    
class UsuarioPatch(BaseModel):
    nombre: Optional[str] = None
    email: Optional[str] = None
    edad: Optional[int] = None

@app.get("/usuarios")
def obtener_usuarios():
    return usuarios_db

@app.get("/usuarios/{usuario_id}")
def obtener_usuario(usuario_id: int):
    for user in usuarios_db:
        if user["id"] == usuario_id:
            return user
    raise HTTPException(status_code=404, detail="404 - Usuario no encontrado")

# PUT para actualizar un usuario completamente
@app.put("/usuarios/{usuario_id}")
def actualizar_usuario_completo(usuario_id: int, usuario: Usuario):
    for i, user in enumerate(usuarios_db):
        if user["id"] == usuario_id:
            usuarios_db[i] = {
                "id": usuario_id, 
                "nombre": usuario.nombre, 
                "email": usuario.email,
                "edad": usuario.edad
                }
            return usuarios_db[i]
    raise HTTPException(status_code=404, detail="404 - Usuario no encontrado")