from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def iniciar_driver():
    """Inicializa y retorna la instancia del navegador Chrome."""
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    return driver

def login_saucedemo(driver, usuario="standard_user", password="secret_sauce"):
    """Navega a saucedemo e inicia sesión con las credenciales proporcionadas."""
    driver.get("https://www.saucedemo.com/")
    
    # Localizar elementos 
    input_user = driver.find_element(By.ID, "user-name")
    input_pass = driver.find_element(By.ID, "password")
    btn_login = driver.find_element(By.ID, "login-button")
    
    # Ingresar credenciales y hacer click
    input_user.clear()
    input_user.send_keys(usuario)
    input_pass.clear()
    input_pass.send_keys(password)
    btn_login.click()