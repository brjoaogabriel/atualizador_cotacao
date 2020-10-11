#       DESCRIÇÃO DO MATERIAL
#___________________________________________________________________
#   Nome:               Extrator de cotação - Google
#   Desenvolvido por:   João Gabriel - @brjoaogabriel
#   Data da últ. att.:  11/10/2020
#   Data da criação:    10/10/2020
#   Descrição:          Extrator utilizado para extrair informação
#                           de ações na api do google
#___________________________________________________________________

#       DESCRIÇÃO DAS BIBLIOTECAS
#___________________________________________________________________
#   os                  > utilizada para limpar a tela
#   Pesquisa_Cotacao    > raspa tela do google
#   Solicita_Ativos     > solicita ativos que o usuário quer extrair
#   Cadastra_Cotacoes   > cadastra as cotações no arquivo csv
#___________________________________________________________________
import os
from google import Pesquisa_Cotacao
from user_interaction import Solicita_Ativos
from data_interaction import Cadastra_Cotacoes

#   Declara ativos que serão buscados no google
ativos = Solicita_Ativos()
os.system('cls')
print("Ativos escolhidos:")
for ativo in ativos:
    print(f"- {ativo}")
print()

#   Declara caminho do arquivo
arquivo = "cotacoes_extraídas.csv"
print(f"Diretório do arquivo:\n{arquivo}\n")

#   Declara o tempo de espera que o usuário acredita ser o ideal para as paginas carregarem
tempo_de_espera = 5
print(f"Tempo de espera:\n{tempo_de_espera}\n")

#   Cadastra as informações dos ativos declarados no arquivo declarado
print("Solicitando as cotações...\n")
Cadastra_Cotacoes(Pesquisa_Cotacao(tempo_de_espera,ativos),arquivo)
print("Rotina finalizada!")