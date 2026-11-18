from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.titulo_productos = (By.CSS_SELECTOR, ".title")
        self.primer_producto_add = (By.ID, "add-to-cart-sauce-labs-backpack")
        self.carrito_badge = (By.CSS_SELECTOR, ".shopping_cart_badge")
        self.icono_carrito = (By.CSS_SELECTOR, ".shopping_cart_link")

    def obtener_titulo(self):
        titulo = self.wait.until(EC.visibility_of_element_located(self.titulo_productos))
        return titulo.text

    def agregar_primer_producto(self):
        boton = self.wait.until(EC.element_to_be_clickable(self.primer_producto_add))
        boton.click()

    def obtener_cantidad_carrito(self):
        badge = self.wait.until(EC.visibility_of_element_located(self.carrito_badge))
        return badge.text

    def ir_al_carrito(self):
        icono = self.wait.until(EC.element_to_be_clickable(self.icono_carrito))
        icono.click()