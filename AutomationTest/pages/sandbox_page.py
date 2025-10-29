from selenium.webdriver.common.by import By
from .base_page import BasePage

class SandboxPage(BasePage):
    ENVIAR_BUTTON = (By.XPATH, "//button[contains(text(),'Enviar')]")
    DYNAMIC_ID_BUTTON = (By.XPATH, "//button[text()='Hacé click para generar un ID dinámico y mostrar el elemento oculto']")
    HIDDEN_TEXT = (By.XPATH, "//p[@id='hidden-element']")
    DEPORTE_DROPDOWN =(By.ID, "formBasicSelect")
    POPUP_BUTTON = (By.XPATH, "//button[text()='Mostrar popup']")
    POPUP_TITLE = (By.ID, "contained-modal-title-vcenter")

    def navigate_sandbox(self):
        self.navigate_to(
            "https://thefreerangetester.github.io/sandbox-automation-testing/"
        )

    def click_enviar(self):
       self.click(self.ENVIAR_BUTTON)

    def click_boton_id_dinamico(self):
        self.click(self.DYNAMIC_ID_BUTTON)

    def hover_over_dynamic_id_button(self):
        self.hover_over_element(self.DYNAMIC_ID_BUTTON)

    def select_checkbox(self, label_text):
        checkbox_locator = (By.XPATH, f"//label[contains(., '{label_text}')]/preceding-sibling::input[@type='checkbox']")
        self.select_element(checkbox_locator)

    def select_radio_button(self, option):
        assert option in ["Si", "No"], "La opción tiene que ser Si o No"
        radio_button_locator =(
            By.XPATH,
            f"//label[text()='{option}']/ancestor::div[1]//input"
        )
        self.hover_over_element(radio_button_locator)
        self.select_element(radio_button_locator)

    def select_deporte(self, deporte):
        self.select_from_dropdown_by_visible_text(self.DEPORTE_DROPDOWN, deporte)

    def get_deporte_dropdown_option(self):
        return self.get_select_options(self.DEPORTE_DROPDOWN)

    def click_boton_popup(self):
        self.hover_over_element(self.POPUP_BUTTON)
        self.click(self.POPUP_BUTTON)

    def get_texto_popup_titulo(self):
        return self.wait_for_element(self.POPUP_TITLE).text

    def get_cell_value(self, fila, columna):
        celda_xpath = \
            f"//h2[text()='Tabla dinámica']/ancestor::div[1]//table//tr[{fila}]//td[{columna}]"
        celda = self.wait_for_element((By.XPATH, celda_xpath))
        return celda.text if celda else None

    def get_cell_value_estatica(self, fila, columna):
        celda_xpath = \
            f"//h2[text()='Tabla estática']/ancestor::div[1]//table//tr[{fila}]//td[{columna}]"
        celda = self.wait_for_element((By.XPATH, celda_xpath))
        return celda.text if celda else None