"""Module to receive text and maniputlate it"""
from interaction_models.data_manipulators_aux.aux_manipulator import AuxManipulator
from typing import List, AnyStr, Dict


class AuxManipulatorLdm(AuxManipulator):
    @staticmethod
    def cleanhtml(raw_html) -> AnyStr:
        clean_html = (
            str(raw_html)
                .replace("R$", "")
                .replace(",", "."))
        return clean_html

    @staticmethod
    def split_in_list(text: str) -> List:
        # waiting existss some case with two or more freights options
        text = text.split(r'teste')
        return text

    @staticmethod
    def split_list(list_to_split: list) -> Dict:
        information = {}
        objects = []

        for index, data_set in enumerate(list_to_split):
            list_to_split[index] = data_set.split(sep='\n')
            if "" in list_to_split[index]:
                list_to_split[index].remove("")
            objects.append(list_to_split[index])

        information["data"] = objects
        return information

    def freight_information(self, raw_html) -> Dict:
        return self.split_list(self.split_in_list(self.cleanhtml(raw_html)))
