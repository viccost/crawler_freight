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
from interaction_models.data_manipulators_aux.aux_manipulator_frp import (
    AuxManipulatorFrp,
)
from typing import Union

commons_exceptions = (
    ec.NoSuchElementException,
    ElementNotInteractableException,
    TimeoutException,
    NoSuchElementException,
    StaleElementReferenceException,
)


class SeleniumFrpInteraction(SeleniumInteraction):
    def __init__(self, browser, cep):
        super().__init__(browser, cep)

    def __clearfield(self) -> None:
        WebDriverWait(self.browser, 12).until(
            ec.presence_of_element_located((By.NAME, "postalCode"))
        )
        element = self.browser.find_element_by_name("postalCode")
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.DELETE)

    def fill_cep_field(self) -> None:
        WebDriverWait(self.browser, 14).until(
            ec.presence_of_element_located((By.NAME, "postalCode"))
        ).send_keys(self.cep)

    def search(self) -> None:
        WebDriverWait(self.browser, 12).until(
            ec.presence_of_element_located((By.NAME, "postalCode"))
        ).send_keys(Keys.ENTER)
        sleep(1.5)
        WebDriverWait(self.browser, 12).until(
            ec.presence_of_element_located(
                (
                    By.CSS_SELECTOR,
                    "body > div.render-container.render-route-store-product > div > div.vtex-store__template.bg-base > "
                    "div > div > div > div:nth-child(6) > div > div:nth-child(3) > div > section > div > "
                    "div.pr0.items-stretch.vtex-flex-layout-0-x-stretchChildrenWidth.flex > div > "
                    "div.vtex-flex-layout-0-x-flexColChild.vtex-flex-layout-0-x-flexColChild--product-col.pb0 > div > "
                    "div.vtex-flex-layout-0-x-flexColChild.pb0 > div > button",
                )
            )
        )

    def get_data(self) -> dict:

        innerHTML = self.browser.find_element(
            By.CSS_SELECTOR,
            "body > div.render-container.render-route-store-product > div > div.vtex-store__template."
            "bg-base > div > div > div > div:nth-child(6) > div > div:nth-child(3) > div > section >"
            " div > div.pr0.items-stretch.vtex-flex-layout-0-x-stretchChildrenWidth.flex > div > "
            "div.vtex-flex-layout-0-x-flexColChild.vtex-flex-layout-0-x-flexColChild--product-col.pb0 "
            "> div > div.vtex-flex-layout-0-x-flexColChild.pb0 > table",
        ).get_attribute("innerHTML")
        cooked = AuxManipulatorFrp().freight_information(innerHTML)
        return cooked

    def initiate(self) -> Union[dict, int]:
        try:
            self.fill_cep_field()
            self.search()
            sleep(1.5)
            self.clearfield()
            data = self.get_data()
            sleep(0.8)
            return data
        except commons_exceptions:
            return 0
