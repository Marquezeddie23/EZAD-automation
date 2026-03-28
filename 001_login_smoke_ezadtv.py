from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeoutError
from dotenv import load_dotenv
import os

# Carga las variables del archivo .env
load_dotenv()

USER = os.getenv("EZAD_USER")
PASSWORD = os.getenv("EZAD_PASSWORD")

def login_ezad():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        print("🌐 Abriendo ezadtv.com/login...")
        page.goto("https://ezadtv.com/login")
        page.wait_for_load_state("networkidle")

        print("📝 Ingresando credenciales...")
        page.fill('input[type="text"], input[name*="user"], input[name*="email"], input[placeholder*="user"], input[placeholder*="User"]', USER)
        page.fill('input[type="password"]', PASSWORD)

        print("☑️  Aceptando términos y condiciones...")
        checkbox = page.locator('input[type="checkbox"]').first
        if not checkbox.is_checked():
            checkbox.check()

        page.wait_for_timeout(500)

        print("🖱️  Haciendo click en Log In...")
        page.get_by_role("button", name="Log In").click()

        page.wait_for_load_state("networkidle")

        current_url = page.url
        if "login" not in current_url:
            print(f"✅ Login exitoso! Redirigido a: {current_url}")
        else:
            print("⚠️  Puede que el login haya fallado. Revisa las credenciales.")

        print("🔍 Aplicando zoom al 33%...")
        page.evaluate("document.body.style.zoom = '33%'")

        print("⏳ Esperando 10 segundos dentro del sitio...")
        page.wait_for_timeout(10000)

        browser.close()
        print("🔒 Navegador cerrado.")

if __name__ == "__main__":
    try:
        login_ezad()
    except PlaywrightTimeoutError:
        print("❌ Timeout: La página tardó demasiado en responder.")
    except Exception as e:
        print(f"❌ Error inesperado: {e}")
