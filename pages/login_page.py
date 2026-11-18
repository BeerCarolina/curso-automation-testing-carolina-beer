from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20) # Aumentamos a 20s para blindarlo contra la congestión del último test
        self.username_input = (By.ID, "user-name")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "login-button")
        self.error_message = (By.CSS_SELECTOR, "[data-test='error']")

    def ingresar_usuario(self, username):
        # Primero esperamos a que el body de la página esté cargado para evitar falsos timeouts en ejecuciones rápidas
        self.wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        
        campo = self.wait.until(EC.presence_of_element_located(self.username_input))
        campo.clear()
        campo.send_keys(username)

    def ingresar_password(self, password):
        campo = self.wait.until(EC.visibility_of_element_located(self.password_input))
        campo.clear()
        campo.send_keys(password)

    def hacer_click_login(self):
        boton = self.wait.until(EC.element_to_be_clickable(self.login_button))
        boton.click()

    def login(self, username, password):
        self.ingresar_usuario(username)
        self.ingresar_password(password)
        self.hacer_click_login()

    def obtener_error(self):
        error = self.wait.until(EC.visibility_of_element_located(self.error_message))
        return error.text