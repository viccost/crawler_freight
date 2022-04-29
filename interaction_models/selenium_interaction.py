import abc
from typing import Dict


class SeleniumInteraction(metaclass=abc.ABCMeta):
    """this class shoould be called by initiate method. The only problem is we have a problem declaring
    abstract private methods. It's also reponsible for return the freight information or return 0 if the
    things don't occur well"""

    def __init__(self, browser, cep):
        self.browser = browser
        self.cep = cep

    @abc.abstractmethod
    def fill_cep_field(self) -> None:
        """Fill the cep input field. Or pass the information by some way"""
        ...

    @abc.abstractmethod
    def search(self) -> None:
        """Start the search, probably by a buttom or a send.Key(ENTER)"""
        ...

    @abc.abstractmethod
    def get_data(self) -> Dict:
        """Manipulate the data, getting from html, text, table whatever. Often needs a manipulator object as support,
        to do the necessaries operations"""
        ...

    @abc.abstractmethod
    def initiate(self) -> Dict:
        """Must be used to call all another methods

        Returns:
        """
        ...
