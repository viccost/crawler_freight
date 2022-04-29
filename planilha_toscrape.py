class FormatoPlanilhaErrado(Exception):
    """Verifique o formato da planilha selecionada"""

    pass


class PlanilhaToScrape:
    from pandas import DataFrame

    def __init__(self, planilha: DataFrame):
        self.spreadsheet = planilha
        self.lower_headers()

    def transformar_em_dict(self) -> list:
        """Transform in list, raises error if the valitation don't set ok"""
        try:
            lista = self.spreadsheet.to_dict(orient="records")
            return lista
        except FormatoPlanilhaErrado:
            raise FormatoPlanilhaErrado()

    def lower_headers(self):
        """Change all spreadsheet's keys to lowercase"""
        for key in self.spreadsheet.keys():
            teste = str.lower(key)
            self.spreadsheet.rename(columns={f"{key}": teste}, inplace=True)


if __name__ == "__main__":
    pass
