import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.funciones import iniciar_driver, login_saucedemo

@pytest.fixture
def driver():
    """Fixture para inicializar y cerrar el navegador por cada test."""
    driver_instance = iniciar_driver()
    yield driver_instance
    driver_instance.quit()


# Test 1
def test_login_exitoso(driver):
    login_saucedemo(driver)
    
   
    WebDriverWait(driver, 10).until(
        EC.url_contains("/inventory.html")
    )
    
    assert "/inventory.html" in driver.current_url
    
    logo = driver.find_element(By.CLASS_NAME, "app_logo")
    assert logo.text == "Swag Labs"

# Test 2
def test_verificacion_catalogo(driver):
    login_saucedemo(driver)
    
    # Validar título de la pestaña/página
    assert "Swag Labs" in driver.title
    
    # Validar presencia de elementos importantes de la interfaz (Menú, Filtro)
    btn_menu = driver.find_element(By.ID, "react-burger-menu-btn")
    filtro = driver.find_element(By.CLASS_NAME, "product_sort_container")
    assert btn_menu.is_displayed()
    assert filtro.is_displayed()
    
    # Comprobar que existan productos visibles y listar el primero
    productos = driver.find_elements(By.CLASS_NAME, "inventory_item")
    assert len(productos) > 0, "No se encontraron productos en el catálogo"
    
    primer_producto_nombre = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
    primer_producto_precio = driver.find_element(By.CLASS_NAME, "inventory_item_price").text
    
    print(f"\n[INFO] Primer producto disponible: {primer_producto_nombre} - Precio: {primer_producto_precio}")

# Test 3

def test_interaccion_carrito(driver):
    login_saucedemo(driver)
    
    # Agrego el primer producto al carrito
    btn_add_cart = driver.find_element(By.XPATH, "(//button[contains(@text, 'Add to cart') or contains(text(), 'Add to cart')])[1]")
    btn_add_cart.click()
    
    # Valida el contador con ícono del carrito
    badge_carrito = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
    assert badge_carrito.text == "1"
    
    # Ir al carrito y verificar que esté el elemento agregado
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    assert "/cart.html" in driver.current_url
    
    item_carrito = driver.find_element(By.CLASS_NAME, "cart_item")
    assert item_carrito.is_displayed()