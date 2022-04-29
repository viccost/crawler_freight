"""Module to receive text and maniputlate it"""
from interaction_models.data_manipulators_aux.aux_manipulator import AuxManipulator
from typing import List, AnyStr, Dict


class AuxManipulatorFrp(AuxManipulator):
    @staticmethod
    def cleanhtml(raw_html) -> AnyStr:
        import re

        clear_remaining_html = re.compile("<.*?>")
        clear_thead = re.compile("<thead.*?/thead>")

        clean_html = re.sub(clear_thead, "", raw_html)

        clean_html = (
            str(clean_html)
                .replace("<td", "$$<td")
                .replace("</tr>", "##")
                .replace("\n", " ")
                .replace("\t", " ")
                .replace("&nbsp;", " ")
        )

        clean_html = re.sub(clear_remaining_html, "", clean_html)
        #  clean_html = "".join(clean_html.strip())
        #  clean_html = re.sub(" +", " ", clean_html)
        return clean_html

    @staticmethod
    def split_in_list(text: str) -> List:
        text = text.split("##")
        text.remove(text[-1])
        return text

    @staticmethod
    def split_list(list_to_split: list) -> Dict:
        information = {}
        objects = []

        for index, data_set in enumerate(list_to_split):
            list_to_split[index] = data_set.split(sep="$$")
            if "" in list_to_split[index]:
                list_to_split[index].remove("")
            objects.append(list_to_split[index])

        information["data"] = objects
        return information

    def freight_information(self, raw_html) -> Dict:
        return self.split_list(self.split_in_list(self.cleanhtml(raw_html)))
