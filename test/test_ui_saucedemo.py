import json
import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


with open("data/datos_login.json", encoding="utf-8") as f:
    DATOS_LOGIN = json.load(f)

@pytest.mark.parametrize("data", DATOS_LOGIN)
def test_login_parametrizado(driver, data):
    login_page = LoginPage(driver)
    login_page.login(data["username"], data["password"])

    if data["valido"]:
        inventory_page = InventoryPage(driver)
        assert "inventory.html" in driver.current_url
        assert inventory_page.obtener_titulo() == "Products"
    else:
        error_text = login_page.obtener_error()
        assert "Epic sadface" in error_text

def test_flujo_agregar_carrito(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    # Login Ok con usuario standard
    login_page.login("standard_user", "secret_sauce")
    
    # Agregar producto y verificar carrito
    inventory_page.agregar_primer_producto()
    assert inventory_page.obtener_cantidad_carrito() == "1"