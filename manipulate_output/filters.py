import abc


class Filter(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def mask(self):
        ...

    @staticmethod
    @abc.abstractmethod
    def name():
        ...


class CheaperFreight(Filter):

    def __init__(self, df):
        self.__mask = (df['preco'] == df['preco'].min())

    @property
    def mask(self):
        return self.__mask

    @staticmethod
    def name():
        return "Cheaper"


class FasterFreight(Filter):
    def __init__(self, df):
        self.__mask = (df['prazo'] == df['prazo'].min())
        self.__name = "Faster"

    @property
    def mask(self):
        return self.__mask

    @staticmethod
    def name():
        return "Faster"
