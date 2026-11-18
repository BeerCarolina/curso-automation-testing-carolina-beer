import pytest
import requests
import logging

BASE_URL = "https://reqres.in/api"

def test_api_get_users():
    logging.info("Ejecutando test de API: GET listado de usuarios")
    response = requests.get(f"{BASE_URL}/users?page=2")
    
    assert response.status_code == 200, f"Se esperaba 200, se obtuvo {response.status_code}"
    
   
    data = response.json()
    assert "data" in data
    assert len(data["data"]) > 0
    assert "email" in data["data"][0]
    logging.info("Test GET de usuarios completado con éxito")

def test_api_post_create_user():
    logging.info("Ejecutando test de API: POST crear usuario")
    payload = {
        "name": "Carolina Beer",
        "job": "QA Automation Engineer"
    }
    response = requests.post(f"{BASE_URL}/users", json=payload)
    
    
    assert response.status_code == 201, f"Se esperaba 201, se obtuvo {response.status_code}"
    
    # Validar contenido de la respuesta
    data = response.json()
    assert data["name"] == "Carolina Beer"
    assert data["job"] == "QA Automation Engineer"
    assert "id" in data
    assert "createdAt" in data
    logging.info("Test POST de creación de usuario completado con éxito")

def test_api_delete_user():
    logging.info("Ejecutando test de API: DELETE eliminar usuario")
    response = requests.delete(f"{BASE_URL}/users/2")
    
    
    assert response.status_code == 204, f"Se esperaba 204, se obtuvo {response.status_code}"
    logging.info("Test DELETE de usuario completado con éxito")