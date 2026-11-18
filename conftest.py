import os
import datetime
import pytest
import logging
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


os.makedirs("logs", exist_ok=True)
logging.basicConfig(
    filename="logs/ejecucion.log",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

@pytest.fixture
def driver(request):
    logging.info(f"Iniciando navegador para el test: {request.node.name}")
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")
    
    # Espera a que el DOM esté completo y el input de usuario visible
    try:
        WebDriverWait(driver, 15).until(
            lambda d: d.execute_script("return document.readyState") == "complete"
        )
        WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located((By.ID, "user-name"))
        )
    except Exception as e:
        logging.error(f"Error al cargar la página de SauceDemo en {request.node.name}: {e}")

    yield driver
    
    logging.info(f"Cerrando navegador para el test: {request.node.name}")
    driver.quit()

# Hook de Pytest para capturar screenshots automáticamente si un test falla
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver_fixture = item.funcargs.get("driver")
        if driver_fixture:
            os.makedirs("reports/assets", exist_ok=True)
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            screenshot_name = f"reports/assets/error_{item.name}_{timestamp}.png"
            driver_fixture.save_screenshot(screenshot_name)
            logging.error(f"Test falló: {item.name}. Captura guardada en: {screenshot_name}")