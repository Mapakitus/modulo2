"""
Los query parameters (parametros de consulta) son datos clave-valor que se utilizan para
filtrar, ordenar y paginar.

Se añaden después de la ruta con un signo de interrogación (?).

Se separan con un ampersand (&)

"""

from fastapi import FastAPI

app = FastAPI()

#Paginación simple
@app.get("/users")
def get_users(limit: int = 10):
    return {
        "users": [f"Usuario {i}" for i in range(1, limit + 1)],
        "total": limit,
        "limit": limit 
    }

#Paginación completa    
@app.get("/products")
def get_products(limit: int = 10, skip: int = 0):
    #Crear una lista de productos con salto y límite
    products = [f"Producto {i}" for i in range(skip + 1, skip + limit + 1)]
    
    return {
        "products": products,
        "total_shown": len(products),
        "limit": limit,
        "skip": skip
    }
    
#Filtrado
@app.get("/items")
def get_items(category: str = "all"):
    if category == "all":
        items = ["Item 1", "Item 2", "Item 3", "Item 4", "Item 5"]
    else:
        items = [f"Item {i} de la categoría {category}" for i in range(1,4)]
        
    return {
        "category": category,
        "items": items,
        "total_shown": len(items)
    }
    
    