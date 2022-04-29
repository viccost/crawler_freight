"""Module to receive text and maniputlate it"""
import abc
from typing import Union


class AuxManipulator(metaclass=abc.ABCMeta):
    """absctract class to receive text and manipulate it, returning a dict"""

    @abc.abstractmethod
    def freight_information(self, raw_html) -> Union[dict[list]]:
        """MUST return a dict: {data: [NOME FRETE, DATE ESTIMATE and PRICE]}"""
        ...
