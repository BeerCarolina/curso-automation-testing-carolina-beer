# Proyecto Final: Automacion de Pruebas (UI & API)

Este repositorio contiene la solucion completa para la pre-entrega y proyecto final de automatizacion de testing, implementando pruebas automatizadas de interfaz de usuario (UI) mediante el patron Page Object Model (POM) y pruebas de servicios web (API Testing), utilizando Python y PyTest.

## Tecnologias y Herramientas Utilizadas

* Lenguaje: Python
* Framework de Testing: PyTest y PyTest-HTML (Reportes detallados)
* Automatizacion Web: Selenium WebDriver 4 (Manejo nativo y esperas explicitas)
* Automatizacion de APIs: Libreria requests
* Arquitectura: Page Object Model (POM) con pruebas data-driven (JSON)
* Monitoreo y Reportes: Logging nativo de Python y captura automatica de pantallas ante fallas.

## Estructura del Proyecto

pre-entrega-automation-testing/
│
├── data/
│   └── datos_login.json         # Datos externos para pruebas parametrizadas
├── logs/
│   └── ejecucion.log            # Registro detallado de la ejecucion de los tests
├── pages/
│   ├── inventory_page.py        # Page Object para la vista de inventario / carrito
│   └── login_page.py            # Page Object para la vista de autenticacion
├── reports/
│   ├── assets/                  # Capturas de pantalla automaticas en caso de fallo
│   └── reporte.html             # Reporte interactivo HTML de la ejecucion
├── test/
│   ├── test_api_reqres.py       # Pruebas de API (GET, POST, DELETE)
│   └── test_ui_saucedemo.py     # Pruebas de UI parametrizadas y flujos de carrito
├── utils/
│   └── funciones.py             # Funciones auxiliares reutilizables
├── conftest.py                  # Configuracion global de fixtures, navegador y hooks de pytest
├── pytest.ini                   # Configuracion del framework pytest
└── README.md                    # Documentacion del proyecto

## Instalacion, Configuracion y Ejecucion

### 1. Instalacion de dependencias
Abre tu terminal en la raiz del proyecto e instala las librerias necesarias ejecutando:

```powershell
pip install selenium pytest pytest-html requests

## 2. Ejecucion de las Pruebas

Para correr todas las pruebas (tanto UI como API) de manera secuencial y generar automaticamente el reporte HTML interactivo, ejecuta el siguiente comando:

`powershell
python -m pytest -v --html=reports/reporte.html

Una vez finalizada la ejecucion, podras encontrar:

El reporte HTML en reports/reporte.html.

El registro de logs en logs/ejecucion.log.

Las capturas de pantalla de evidencia (en caso de fallas) dentro de reports/assets/.

## 3. Cómo Instalar las Dependencias
 Clonar el repositorio localmente:
   git clone [https://github.com/BeerCarolina/curso-automation-testing-carolina-beer.git]
