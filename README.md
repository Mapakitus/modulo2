## CÓMO CREAR UN ENTORNO VIRTUAL EN VISUAL STUDIO CODE

1. Abrir la paleta de comandos: CTRL+SHIFT+P

2. Buscar "environment" o "ambiente", según el idioma.

3. Hacemos "click" en python: Create Environment.

4. Seleccionar el tipo de environment, para este caso "venv"

5. Seleccionar el intérprete de Python, la versión, he elegido la última que tengo. 3.14

6. Se va creando y finalmente lo comprobamos en el arbol de directorios, que está .venv

## Si aparece un error de windows en la consola.

1. En la barra de windows, buscar powershell y ejecutar el siguiente comando: "Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser"

Así reinicias VSCode y ya no da error.

## Para instalarlo, en la terminal ejecutamos:
 pip install -r requirements.txt

 ## Para ejecutar el main.py por ejemplo haríamos lo siguiente:

 **python main.py**

 * Ejecutar en la terminal -> uvicorn main:app --reload

 ## Si se trata del fichero prueba.py dentro de la carpeta metodos_GET

 * uvicorn metodos_GET.prueba:app --reload

 * Se pone uvicorn nombre_Carpeta.nombre_fichero:app --reload

 ##