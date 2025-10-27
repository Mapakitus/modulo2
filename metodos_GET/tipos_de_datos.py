from fastapi import FastAPI

#creamos la instancia de la aplicación FastAPI
app = FastAPI()


@app.get("/")
def leer_raiz():
    return {"mensaje": "Vamos a ver los tipos de datos en FastAPI"}

@app.get("/tipos-datos")
def mostrar_tipos():
    return{
        "texto": "Hola, grajillas",
        "numero_entero": 23,
        "numero_decimal": 3.1,
        "booleano": True,
        "lista_numero": [1, 2, 3, 4, 5],
        "lista_texto": ["uno", "dos", "tres"],
        "lista_booleanos": [True, False, True],
        "lista_variada": [1, "dos", True, 3.14],
        "valor_nulo": None,
        "tupla": (1, 2, 3),
        "conjunto": {1, 2, 45, 65, 78},
        "diccionario": {"nombre": "Paco", 
                        "edad": 23, 
                        "calle": "Josep Serra Carsi"}
    }