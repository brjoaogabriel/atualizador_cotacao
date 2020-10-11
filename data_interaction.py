#___________________________________________________________________
#   Nome:               Extrator de cotação - Google
#   Desenvolvido por:   João Gabriel - @brjoaogabriel
#   Data da últ. att.:  11/10/2020
#   Data da criação:    10/10/2020
#   Descrição:          Utilizado para cadastrar as linhas csv
#                           no arquivo
#___________________________________________________________________

#       DESCRIÇÃO DAS BIBLIOTECAS
#___________________________________________________________________
#   datetime            > cadastrar data no csv
import datetime

def Cadastra_Cotacoes(informacoes,arquivo):

    #   DESCRIÇÃO DOS INPUTS...
    #       Informacoes > Dicionário contendo as informações do ativo
    #       Arquivo     > Caminh odo arquivo que será lido e alterado

    #   Le o tamanho do arquivo
    print("Lendo o arquivo...")
    with open(arquivo,'r') as arq:
        tamanho_arq = len(arq.read())

    #   Cadastra as informações
    with open(arquivo,'a') as arq:

        #   Itera as informações de cada ativo para montar uma linha csv

        #   Valida se o arquivo está vazio ou não para cadastrar o cabeçalho
        if tamanho_arq == 0:
            print("Cadastrando cabeçalho...")
            cabeçalho_csv = ""
            for campo in informacoes[0]:
                cabeçalho_csv += f"{campo}|"
            cabeçalho_csv = cabeçalho_csv[0:len(cabeçalho_csv)-1] + "\n"
            arq.write(cabeçalho_csv)
            
        for informacao in informacoes:
            #   Cria a linha CSV
            linha_csv = ""
            for campo in informacao:
                linha_csv += f"{informacao[campo].replace('-','')}|"

            #   Monta a linha csv contendo a data de hoje em MM/DD/YYYY
            hoje = f"""{datetime.datetime.today().month}/{datetime.datetime.today().day}/{datetime.datetime.today().year}"""
            linha_csv += f"{hoje}"

            print(f"Linha CSV: {linha_csv}")

            #   Escreve a linha csv no arquivo
            print("Escrevendo a linha csv...")
            arq.write(f"{linha_csv}\n")

    return True