import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
import allure

@allure.title("El boton muestra un text luego de hacer clic en boton dinamico")
@allure.epic("Interfaz Web")
@allure.feature("Boton con ID dinamico")
@pytest.mark.regresion
def test_validar_texto_oculto_boton_dinamico(sandbox_page):
    sandbox_page.navigate_sandbox()
    #sandbox_page.click_enviar()
    sandbox_page.click_boton_id_dinamico()
    elemento_texto_oculto =  sandbox_page.wait_for_element(
        sandbox_page.HIDDEN_TEXT
    )
    texto_esperado = "OMG, aparezco después de 3 segundos de haber hecho click en el botón"
    assert texto_esperado in elemento_texto_oculto.text, "No coincide el texto oculto"

@pytest.mark.regresion
def test_boton_id_dinamico_cambio_color(sandbox_page):
    sandbox_page.navigate_sandbox()

    boton_id_dinamico = sandbox_page.wait_for_element(sandbox_page.DYNAMIC_ID_BUTTON)

    # obtenemos el color previo
    color_antes = boton_id_dinamico.value_of_css_property("background-color")
    sandbox_page.hover_over_dynamic_id_button()
    # obtener color diferente
    color_despues = boton_id_dinamico.value_of_css_property("background-color")

    # validacion final
    assert color_antes != color_despues

@pytest.mark.regresion
def test_elegir_check(sandbox_page):
    sandbox_page.navigate_sandbox()
    sandbox_page.select_checkbox('Pasta')

@pytest.mark.regresion
def test_elegir_radio_button(sandbox_page):
    sandbox_page.navigate_sandbox()
    sandbox_page.select_radio_button('Si')

@pytest.mark.regresion
def test_elegir_un_deporte(sandbox_page):
    sandbox_page.navigate_sandbox()
    sandbox_page.select_deporte('Fútbol')

@pytest.mark.regresion
def test_deportes_options(sandbox_page):
    sandbox_page.navigate_sandbox()
    options = sandbox_page.get_deporte_dropdown_option()
    expected_options = ['Seleccioná un deporte', 'Fútbol', 'Tennis', 'Basketball']

    assert options == expected_options

@pytest.mark.regresion
def test_popup_title(sandbox_page):
    sandbox_page.navigate_sandbox()
    sandbox_page.click_boton_popup()
    popup_title = sandbox_page.get_texto_popup_titulo()
    expected_popup_title = "Popup de ejemplo"
    assert popup_title == expected_popup_title, f"El texto del popup es incorrecto"

@pytest.mark.regresion
def test_valor_celda_cambia(sandbox_page):
    sandbox_page.navigate_sandbox()
    valor_inicial  = sandbox_page.get_cell_value(2,3)
    sandbox_page.reload_page()
    valor_final  =sandbox_page.get_cell_value(2,3)
    assert valor_final != valor_inicial

@allure.title("Validar que las celdas queden iguales despues de recargar")
@pytest.mark.regresion
def test_valor_celda_queda_igual(sandbox_page):
    with allure.step("Dado que navego al sandbox y tomo el valor inicial de la tabla estatica"):
        sandbox_page.navigate_sandbox()
        valor_inicial  = sandbox_page.get_cell_value_estatica(2,3)
    with allure.step("Cuando se recarga la pagina y tomo el valor de la misma tabla"):
        sandbox_page.reload_page()
        valor_final  =sandbox_page.get_cell_value_estatica(2,3)
    with allure.step("Puedo verificar que el valor no cambia"):
        assert valor_final == valor_inicial