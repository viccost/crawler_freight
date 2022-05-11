from salvar_ajustar import salvar_ajustar as sv
from selenium import webdriver
import pandas as pd
from chrome_options import ChromeOptions
from interaction_models.selenium_interaction_frp import SeleniumFrpInteraction
from interaction_models.selenium_interaction_dtr import SeleniumDtrInteraction
from interaction_models.selenium_interaction_l import SeleniumLdmInteraction

from output_data import SpreadsheetOutputData


def get_spreadsheet_to_scrape() -> pd.DataFrame:
    """choose the file that contains the data for scrapinG"""
    planilha_to_scrape = sv.gerar_dataframe(sv.escolher_arquivo())
    planilha_to_scrape = planilha_to_scrape.fillna(" ")
    return planilha_to_scrape


def get_page():
    planilha_to_scrape = sv.gerar_dataframe(sv.escolher_arquivo())
    planilha_to_scrape = planilha_to_scrape.fillna(" ")
    return planilha_to_scrape


def transform_in_dict(planilha_to_scrape):
    import planilha_toscrape

    try:
        to_scraping = planilha_toscrape.PlanilhaToScrape(
            planilha_to_scrape
        ).transformar_em_dict()
        return to_scraping
    except planilha_toscrape.FormatoPlanilhaErrado:
        print(
            "Houve um problema ao transformar seus dados! Tente verificar o nome de suas colunas"
        )
        exit()


def iniciar_chrome() -> webdriver.Chrome:
    chrome_options = ChromeOptions().chrome_options
    driver = webdriver.Chrome(options=chrome_options)
    return driver


output = SpreadsheetOutputData()


def main():
    planilha_to_scrape = get_spreadsheet_to_scrape()
    chrome = iniciar_chrome()
    url = ""
    to_scraping = transform_in_dict(planilha_to_scrape)

    # settings
    interaction_model = SeleniumLdmInteraction

    cont = 0
    for record_to_collect in to_scraping:
        cont += 1
        print(cont)
        cep = record_to_collect["cep"]
        cod = record_to_collect["código"]
        range_cep = record_to_collect["range"]
        link = record_to_collect["link"]

        # there is a problem here, if we get an error simulating the execution
        # in this way it never refresh the actual page
        if record_to_collect["link"] != url:
            url = record_to_collect["link"]
            chrome.get(record_to_collect["link"])

        our_interaction = interaction_model(chrome, cep)
        result = our_interaction.initiate()

        if result != 0:
            for data in result["data"]:
                output.add_collected_data(
                    cod, cep, range_cep, link, data[0], data[1], data[2]
                )
        else:
            output.add_url_error(cod, cep, range_cep, link)
            print("Ocorreu um erro")

    output.save_collected_data()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        output.save_collected_data()
