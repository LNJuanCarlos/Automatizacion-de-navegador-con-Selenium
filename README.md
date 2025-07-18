Crear carpeta y entorno virtual

-> mkdir automatizacion_web
-> cd automatizacion_web
-> python -m venv venv

Activar entorno virtual:

Windows:
.\venv\Scripts\activate

Linux/macOS:
source venv/bin/activate

Instalar Selenium y el controlador de Chrome

pip install selenium

Descargar ChromeDriver:

-> Ve a https://chromedriver.chromium.org/downloads

-> Descarga la versión que coincida con tu versión de Google Chrome.

-> Extrae el ejecutable chromedriver.exe.

-> Colócalo en la carpeta de tu proyecto o en una carpeta del PATH del sistema.

-> Crear tu primer script

-> Crear un archivo -> buscar_google.py 

Ejecutar

python buscar_google.py

-> Y verás cómo se abre el navegador, busca en Google y te muestra los resultados en consola.

////////////////////////////////////////////////////////////////////
////////////////////////NUEVO ARCHIVO//////////////////////////////
//////////////////////////////////////////////////////////////////

Iniciar sesión automáticamente en un sitio web

Automatizar el proceso de inicio de sesión en un sitio de prueba:

Usaremos este sitio seguro y gratuito para practicar:

https://the-internet.herokuapp.com/login

-> Crear un nuevo archivo login_demo.py

Puedes Ejecutar tambien:

python login_demo.py
