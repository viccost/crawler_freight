from selenium.webdriver import Keys
from time import sleep
from interaction_models.selenium_interaction import SeleniumInteraction
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.common.exceptions import (
    ElementNotInteractableException,
    TimeoutException,
    NoSuchElementException,
    StaleElementReferenceException,
)
from interaction_models.data_manipulators_aux.aux_manipulator_dtr import (
    AuxManipulatorDtr,
)
from typing import Union, Dict
from bs4 import BeautifulSoup

commons_exceptions = (
    ec.NoSuchElementException,
    ElementNotInteractableException,
    TimeoutException,
    NoSuchElementException,
    StaleElementReferenceException,
)


class SeleniumDtrInteraction(SeleniumInteraction):
    def __init__(self, browser, cep):
        super().__init__(browser, cep)

    def __clearfield(self) -> None:
        WebDriverWait(self.browser, 14).until(
            ec.presence_of_element_located((By.ID, "btn-limpar-calculo-frete"))
        ).click()

    def __pegar_html_selenium(self) -> BeautifulSoup:
        html = self.browser.page_source
        pagina_navegador = BeautifulSoup(html, features="lxml")
        return pagina_navegador

    def __waiting_the_response(self) -> int:
        tie = 0
        while True:
            tie += 1
            browser_page = self.__pegar_html_selenium()
            ready_search = str(browser_page.find("div", class_="div-btn-limpa-calculo-frete"))
            if "display:block" in ready_search:
                return 200
            if tie == 15:
                return 0
            sleep(1.2)

    def fill_cep_field(self) -> None:
        WebDriverWait(self.browser, 14).until(
            ec.presence_of_element_located((By.ID, "vcCepCalculoFrete"))
        ).send_keys(self.cep)

    def search(self) -> None:
        WebDriverWait(self.browser, 12).until(
            ec.presence_of_element_located((By.ID, "vcCepCalculoFrete"))
        ).send_keys(Keys.ENTER)

    def get_data(self) -> Dict:
        text_to_manipulate = {"data": [""]}
        innerHTML = self.browser.find_element(
            By.CLASS_NAME, "tb-retorno-frete"
        ).get_attribute("innerHTML")
        text_to_manipulate = AuxManipulatorDtr().freight_information(innerHTML)
        return text_to_manipulate

    def initiate(self) -> Union[dict, int]:
        try:
            self.fill_cep_field()
            self.search()
            response = self.__waiting_the_response()
            if response == 200:
                data = self.get_data()
            else:
                sleep(0.8)
                data = 0
            self.__clearfield()
            return data

        except commons_exceptions:
            return 0
