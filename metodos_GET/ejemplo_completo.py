from fastapi import FastAPI

#creamos la instancia de la aplicación FastAPI
app = FastAPI()


@app.get("/perfil-completo")
def obtener_perfil():
    return {
        "usuario": {
            "nombre": "La Grajilla",
            "apellido": "Occidental",
            "edad": 27,
            "email": "grajilla@occidental.com",
            "telefono": "123 45 67 89"
                    },
        "configuracion": {
            "tema": "oscuro",
            "notificaciones": True,
            "idioma": "español",
            "zona_horaria": "Madrid"
                        },
        "estadisticas": {
            "visitas": 15,
            "compras": 2,
            "ultimo acceso": "2025-10-27"

                        }
            }