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