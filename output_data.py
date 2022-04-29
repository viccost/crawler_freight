"""class that defines the output format off collected data"""

from pandas import DataFrame
import salvar_ajustar.salvar_ajustar as sv


class SpreadsheetOutputData:
    """class that defines the output format off collected data"""

    dataFrameDict = {
        "cod": [],
        "cep": [],
        "range": [],
        "link": [],
        "transportadora": [],
        "prazo": [],
        "preco": [],
    }

    def __init__(self):
        pass

    @staticmethod
    def getdata():
        from datetime import datetime

        return datetime.now().strftime("%d-%m-%Y %H-%M-%S")

    def add_url_error(self, cod, cep, range_prd, link) -> None:
        error_message = "problem checking"
        self.dataFrameDict["cod"].append(cod)
        self.dataFrameDict["cep"].append(cep)
        self.dataFrameDict["range"].append(range_prd)
        self.dataFrameDict["link"].append(link)
        self.dataFrameDict["transportadora"].append(error_message)
        self.dataFrameDict["prazo"].append(error_message)
        self.dataFrameDict["preco"].append(error_message)

    def add_collected_data(
        self, cod, cep, range_prd, link, transportadora, prazo, preco
    ) -> None:
        self.dataFrameDict["cod"].append(cod)
        self.dataFrameDict["cep"].append(cep)
        self.dataFrameDict["range"].append(range_prd)
        self.dataFrameDict["link"].append(link)
        self.dataFrameDict["transportadora"].append(transportadora)
        self.dataFrameDict["prazo"].append(prazo)
        self.dataFrameDict["preco"].append(preco)

    def save_collected_data(self) -> None:

        dataFrame = DataFrame.from_dict(self.dataFrameDict)
        sv.salvar_arquivo_planilha(dataFrame, f"Scrape {self.getdata()}", "xlsx")
