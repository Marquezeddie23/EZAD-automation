EZAD Automation 🤖
Automatización de pruebas para ezadtv.com usando Python y Playwright.
🚀 Tecnologías

Python 3.12
Playwright 1.58

📋 Requisitos
Instalar dependencias:
bashpip install playwright python-dotenv
playwright install
⚙️ Configuración

Copia el archivo de ejemplo y llena tus credenciales:

bashcp .env.example .env

Edita el .env con tus datos:

EZAD_USER=tu_usuario
EZAD_PASSWORD=tu_contraseña
🧪 Tests disponibles
ArchivoDescripción001_login_smoke_ezadtv.pySmoke test — verifica que el login funciona correctamente
▶️ Cómo correr
bashpython 001_login_smoke_ezadtv.py
🔒 Seguridad
Las credenciales se manejan con variables de entorno. El archivo .env está en .gitignore y nunca se sube al repositorio.
