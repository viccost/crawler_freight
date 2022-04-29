"""Module to receive text and maniputlate it"""
from interaction_models.data_manipulators_aux.aux_manipulator import AuxManipulator


class AuxManipulatorDtr(AuxManipulator):
    @staticmethod
    def cleanhtml(raw_html):
        import re

        CLEANR = re.compile("<.*?>")

        clean_html = (
            str(raw_html)
            .replace("<td>", "##")
            .replace("</tr>", "##")
            .replace("\n", "")
            .replace("\t", "")
        )
        clean_html = "".join(clean_html.strip())
        clean_html = re.sub(CLEANR, "", clean_html)
        clean_html = re.sub(" +", " ", clean_html)
        return clean_html

    @staticmethod
    def split_in_list(text: str):
        text = text.split("##")
        text.remove(text[-1])
        return text

    @staticmethod
    def split_list(list_to_split: list) -> dict:
        information = {}
        objects = []
        if "" in list_to_split:
            list_to_split.remove("")
        if len(list_to_split) >= 6:
            first_list = list_to_split[list_to_split.index(" ") + 1:]
            second_list = list_to_split[: list_to_split.index(" ")]
            objects.append(first_list)
            objects.append(second_list)
        else:
            objects.append(list_to_split)
        information["data"] = objects
        return information

    def freight_information(self, raw_html) -> dict:

        return self.split_list(self.split_in_list(self.cleanhtml(raw_html)))
