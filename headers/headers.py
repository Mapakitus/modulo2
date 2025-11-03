from fastapi import FastAPI, Header


app = FastAPI()

@app.get("/preferencias/")
def obtener_preferencias(
    accept_language: str = Header(default="es-ES"),
    accept_encoding: str = Header(default="gzip")
):
    return {
        "idioma_preferido": accept_language,
        "codificacion_aceptada": accept_encoding  
    }