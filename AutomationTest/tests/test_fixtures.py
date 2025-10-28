import csv

import pytest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# setear datos, parametrizacion
#@pytest.fixture(params=['Playwright', 'Selenium', 'Cypress'])
#def termino_de_busqueda(request):
#   return request.param

#setear datos desde un archivo externo, leer
def read_search_terms():
    with open('TestData/busquedaGoogle.csv', newline='') as csvfile:
         data = list(csv.reader(csvfile))
    # devolver terminos sin el titulo
    return [row[0] for row in data[1:]]

 #Fixture para parametrizar terminos de busqueda
@pytest.fixture(params=read_search_terms())
def termino_de_busqueda(request):
    return request.param

# configurar driver y browser
@pytest.fixture()
def browser():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get("https://www.google.com/")
    yield driver
    driver.quit()

# caso de prueba
def test_google_busqueda(browser, termino_de_busqueda):
    search_box = browser.find_element("name", "q")
    search_box.send_keys(termino_de_busqueda + Keys.ENTER)
    results = browser.find_element("id", "search")
    assert len(results.find_elements("xpath", ".//div")) > 0, "Hay resultados de búsqueda"
