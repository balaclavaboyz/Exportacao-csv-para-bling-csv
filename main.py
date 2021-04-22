import os

import requests
import pandas as pd
import chardet
from csv import writer

#TODO preencher o campo: Classificacao_fiscal
#TODO integracao com o API para automatizacao
#TODO receber args para o input de nomes dos arquivos


quantidade_de_items_finais = 20
nome_do_arquivo_final = 'blingcsv.csv'
nome_do_arquivo_original = 'PRODUTO MILVEST 20 04 2021 15 23.csv'


def append_list_as_row(file_name, list_of_elem):
    # Open file in append mode
    with open(file_name, 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        csv_writer = writer(write_obj)
        # Add contents of list as last row in the csv file
        csv_writer.writerow(list_of_elem)


class Dados:
    lista_referencia = []
    lista_item = []
    lista_descricao = []
    lista_validade = []
    lista_data = []
    lista_preco1 = []
    lista_preco2 = []
    lista_preco3 = []
    lista_preco4 = []


def lercsv_converterdata_ordenardata():
    original = pd.read_csv(nome_do_arquivo_original, error_bad_lines=False, encoding='ansi',
                           low_memory=False,
                           delimiter=';', header=0)
    original['DATA'] = pd.to_datetime(original.DATA, dayfirst=True)
    sorted_date = original.sort_values(by=['DATA'], ascending='false')
    return sorted_date


def processarDado(sorted_date):
    items = sorted_date.tail(quantidade_de_items_finais)

    temp = Dados()
    for index, row in items.iterrows():
        temp.lista_referencia.append(row['REFERENCIA'])
        temp.lista_item.append(row['ITEM'])
        temp.lista_descricao.append(row['DESCRICAO'])
        temp.lista_validade.append(row['VALIDADE'])
        temp.lista_data.append(row['DATA'])
        temp.lista_preco1.append(row['PRECO1'])
        temp.lista_preco2.append(row['PRECO2'])
        temp.lista_preco3.append(row['PRECO3'])
        temp.lista_preco4.append(row['PRECO4'])

    return temp


def printar_props(this):
    print(this.lista_referencia)
    print(this.lista_item)
    print(this.lista_descricao)
    print(this.lista_validade)
    print(this.lista_data)
    print(this.lista_preco1)
    print(this.lista_preco2)
    print(this.lista_preco3)
    print(this.lista_preco4)


def ler_modelo_bling():
    modelo = pd.read_csv('modelo.csv', encoding='ISO-8859-1')
    # for word in modelo.columns:
    #     print(word + ' = []')
    return modelo


def criar_arquivo_csvparabling_com_header_pronto(path):
    if os.path.isfile(path):
        os.remove(path)

    f = open(path, 'x')

    header = [
        "ID",
        "Codigo",
        "Descricao",
        "Unidade",
        "Classificacao_fiscal",
        "Origem",
        "Preco",
        "Valor_IPI_fixo",
        "Observacoes",
        "Situacao",
        "Estoque",
        "Preco_de_custo",
        "Cod_no_fornecedor",
        "Fornecedor",
        "Localizacao",
        "Estoque_maximo",
        "Estoque_minimo",
        "Peso_liquido_kg",
        "Peso_bruto_kg",
        "GTIN_EAN",
        "GTIN_EAN_da_" "embalagem",
        "Largura_do_ Produto",
        "Altura_do_Produto",
        "Profundidade_do_produto",
        "Data_Validade",
        "Descricao_do_Produto_no_Fornecedor",
        "Descricao_Complementar",
        "Unidade_por_Caixa",
        "Produto_Variacao",
        "Tipo_Producao",
        "Classe_de_enquadramento_do_IPI",
        "Codigo_da_lista_de_servicos",
        "Tipo_do_item,Grupo de Tags/Tags",
        "Tributos",
        "Código Pai",
        "Código Integração",
        "Grupo de Produtos",
        "Marca",
        "CEST",
        "Volumes",
        "Descriçãoo curta",
        "Cross-Docking",
        "URL Imagens Externas",
        "Link Externo",
        "Meses Garantia",
        "Clonar dados do pai",
        "Condição do produto",
        "Frete Grátis",
        "Número FCI",
        "Vídeo",
        "Departamento",
        "Unidade de medida",
        "Preço de compra",
        "Valor base ICMS ST para retenÃ§Ã£o",
        "Valor ICMS ST para retenção",
        "Valor ICMS próprio do substituto",
    ]

    append_list_as_row(path, header)


def integracao(objecto_final):
    criar_arquivo_csvparabling_com_header_pronto(nome_do_arquivo_final)

    for j in range(len(objecto_final.lista_referencia)):
        novalinha = [
            "",
            objecto_final.lista_referencia[j],
            objecto_final.lista_descricao[j],
            "UN",
            "",
            0,
            objecto_final.lista_preco1[j],
            0,
            "",
            "Ativo",
            0,
            0,
            "",
            "",
            "",
            0,
            0,
            0,
            0,
            objecto_final.lista_validade[j],
            "",
            "",
            0,
            "Produto",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            0,
            "",
            "",
            0,
            0,
            0,
            0,
            "",
            "",
            0,
            "Não",
            "NOVO",
            "Não",
            "",
            "",
            "",
            "",
            0,
            0,
            0,
            0,
        ]
        append_list_as_row('blingcsv.csv', novalinha)


def printar_o_csv(path):
    arquivo = pd.read_csv(path)
    print(arquivo.to_string())

def main():

    csvsorted = lercsv_converterdata_ordenardata()
    objecto_final = processarDado(csvsorted)

    # printar_props(objecto_final)

    integracao(objecto_final)

    printar_o_csv(nome_do_arquivo_final)


if __name__ == "__main__":
    main()
