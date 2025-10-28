import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains

@pytest.mark.sandbox
def test_validar_texto_oculto_boton_dinamico(sandbox_page):
    sandbox_page.navigate_sandbox()
    #sandbox_page.click_enviar()
    sandbox_page.click_boton_id_dinamico()
    elemento_texto_oculto =  sandbox_page.wait_for_element(
        sandbox_page.HIDDEN_TEXT
    )
    texto_esperado = "OMG, aparezco después de 3 segundos de haber hecho click en el botón"
    assert texto_esperado in elemento_texto_oculto.text, "No coincide el texto oculto"

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