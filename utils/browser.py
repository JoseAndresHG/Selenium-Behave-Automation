from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


def select_browser(browser_name, options=None):
    # 1. Corregimos el nombre de la variable (usamos browser_name)
    if not browser_name:
        browser_name = 'chrome'
    else:
        browser_name = browser_name.lower()

    # 2. Inicialización correcta de los drivers
    if browser_name == "chrome":
        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)

    elif browser_name == "firefox":
        service = FirefoxService(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service)

    elif browser_name == "edge":
        service = EdgeService(EdgeChromiumDriverManager().install())
        driver = webdriver.Edge(service=service)

    else:
        # Aquí también corregimos el nombre de la variable para el error
        raise ValueError(f"Navegador '{browser_name}' no soportado.")

    driver.maximize_window()
    return driver


# --- Ejemplo de uso ---
#if __name__ == "__main__":
    # Puedes cambiar "chrome" por "firefox" o "edge"
   # mi_driver = iniciar_navegador("chrome")

   # mi_driver.get("https://www.google.com")
  #  print(f"Título de la página: {mi_driver.title}")

   # mi_driver.quit()