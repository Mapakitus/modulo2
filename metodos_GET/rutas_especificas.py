"""
Cada ruta representa un recurso o funcionalidad diferente.

Buenas prácticas:
- En rutas usar nombres en plural para colecciones (/productos, /usuarios, /animales)
- Nombres en minúscula
"""

from fastapi import FastAPI

app = FastAPI()

# ruta raíz
@app.get("/")
def leer_raiz():
    return {"mensaje": "La ruta raíz de nuestra apliación"}

# ruta de productos
@app.get("/productos")
def obtener_productos():
# devolvemos una lista de productos
    return {"productos": ["Leche", "Queso", "Manzana", "Limpiacristales"]}