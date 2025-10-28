"""
Los path parameters (parámetros de ruta) son variables que forman parte de la URL del endpoint.

- Ruta: /users/{user_id}
- Función: def get_user(user_id)
- URL: /users/1     
"""
from fastapi import FastAPI

app = FastAPI()

@app.get("/users/{user_id}")
def get_user(user_id):
    return {
        "user_id": user_id,
        "name": f"Usuario {user_id}",
        "email": f"usuario{user_id}@gmail.com",
        "status": "activo" 
    }
    
@app.get("/products/{product_id}")
def get_product(product_id):
    return {
        "product_id": product_id,
        "name": f"Producto {product_id}",
        "price": 5.99,
        "description": f"Descripción del producto {product_id}"
    }

@app.get("/categories/{category_name}")
def get_category(category_name):
    return {
        "category": category_name,
        "name": f"Categoría {category_name}",
        "description": f"Productos de la categoría {category_name}",
        "stock": 23
    }