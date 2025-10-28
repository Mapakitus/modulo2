"""
Crea un endpoint en FastAPI que permita obtener información de un usuario específico utilizando tanto path parameters como query parameters.

Debes crear:

Un endpoint con la ruta /users/{user_id} donde user_id es un path parameter de tipo entero
El endpoint debe aceptar dos query parameters opcionales:
include_email: booleano con valor por defecto False
format: string con valor por defecto "basic"
La función debe devolver un diccionario con:
user_id: el ID del usuario recibido como path parameter
name: un string que diga "Usuario {user_id}"
email: solo si include_email es True, devolver "user{user_id}@example.com"
format: el valor del query parameter format recibido
Para empezar, importa FastAPI, crea la instancia de la aplicación con app = FastAPI(), y define tu función con el decorador @app.get() especificando la ruta correcta. Recuerda que los path parameters se indican con llaves {} en la ruta y los query parameters son parámetros adicionales de la función con valores por defecto.    
    
"""

from fastapi import FastAPI

app = FastAPI()

# Escribe aquí tu endpoint
@app.get("/users/{user_id}")
def get_user(user_id: int, include_email: bool = False, format: str = "basic"):
    user_info = {
        "user_id": user_id,
        "name": f"Usuario {user_id}",
        "format": format
    }
    
        #Solo añadir email si include_email es True
    if include_email:
            user_info["email"] =  f"user{user_id}@example.com"
    
    return user_info


"""
#Usando comprensión de diccionario con el operdador de desempaquetado **
@app.get("/users/{user_id}")
def get_user(user_id: int, include_email: bool = False, format: str = "basic"):
    return {
        "user_id": user_id,
        "name": f"Usuario {user_id}",
        "format": format,
        **({"email": f"user{user_id}@example.com"} if include_email else {})
    }
"""