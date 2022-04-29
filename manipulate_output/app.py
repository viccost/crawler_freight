from salvar_ajustar import salvar_ajustar as sv
from pandas import to_numeric, concat, DataFrame
from filters import CheaperFreight, FasterFreight, Filter
from typing import List

database = sv.gerar_dataframe(sv.escolher_arquivo())
unique_values = database['SKU'].unique().tolist()

# first step
database['preco'].replace(',', '.', inplace=True, regex=True)
database['preco'].replace('Grátis', 0, inplace=True, regex=True)

# second step
database['preco'] = to_numeric(database['preco'], errors='ignore', downcast='float')


def filtering(df: DataFrame, mask):
    """This function must receive a DataFrame that cointains, at least, columns SKU, prazo and preco. Also a filter
    option to apply on df and then return the result.
    :param df: Dataframe to filter
    :param mask: A filter class.
    :returns: Filtered dataframe param"""
    new_df = 0

    for value in unique_values:
        sku_mask = (df['SKU'] == value)
        df_sku_in_analyses = database[sku_mask]
        mask_to_aplicate = mask(df_sku_in_analyses).mask

        # get min price
        if type(new_df) != DataFrame:
            new_df = df_sku_in_analyses[mask_to_aplicate]
        else:
            new_df = concat([new_df, df_sku_in_analyses[mask_to_aplicate]])

    return new_df


def split_by_range(df: DataFrame, name: str) -> List:
    """Split the all database by range and return them in list, with Name and Dataframe to be saved using
    salvar_planilhas."""
    grouped = dict(tuple(df.groupby('range')))
    all_ranges = df['range'].unique().tolist()
    dataframes_to_save = []
    for value in all_ranges:
        dataframes_to_save.append({"Nome": f"{name} Range {value}", "Dataframe": grouped[value]})
    return dataframes_to_save


# STRATEGY

mask = CheaperFreight
new_database = filtering(database, mask)

# treating preco data
new_database['preco'] = new_database['preco'].apply(lambda x: float("{:.2f}".format(x)))
new_database['preco'] = new_database['preco'].apply(lambda x: "Grátis" if x == 0 else x)
new_database['prazo'] = new_database['prazo'].apply(lambda x: "2 a 5 dias" if x == "lojas" else x)

pack_to_save = split_by_range(new_database, mask.name())
sv.salvar_planilhas(pack_to_save)
