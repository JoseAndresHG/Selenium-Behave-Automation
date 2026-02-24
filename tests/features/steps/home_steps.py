from behave import step
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
from utils.locators import RegistrationLocators


@step("Abrir pagina {url}")
def step_impl(context, url):
    context.driver.get(url)


@step('hago click en el botón de "{nombre_boton}"')
def step_impl(context, nombre_boton):
    elementos = {
        "Registro": "//a[contains(@class,'ico-register')]",
        "Genero": "//input[@value='M']",
        "registro": "///input[@name='register-button']",
        "Contacto": "//a[text()='Contact us']",
        "BTN_REGISTER_SUBMIT" : "//input[@name='register-button']"
    }
    xpath = elementos.get(nombre_boton)

    if not xpath:
        raise ValueError(f"El botón '{nombre_boton}' no está definido en el diccionario.")

    boton = WebDriverWait(context.driver, 10).until(
        ec.element_to_be_clickable((By.XPATH, xpath))
    )
    boton.click()


@step('diligencio "{texto}" en el campo "{nombre_variable}"')
def step_impl(context, texto, nombre_variable):
    xpath = getattr(RegistrationLocators, nombre_variable)

    elemento = WebDriverWait(context.driver, 5).until(
        ec.element_to_be_clickable((By.XPATH, xpath))
    )
    elemento.clear()
    elemento.send_keys(texto) # Aquí se usa el valor dinámico


