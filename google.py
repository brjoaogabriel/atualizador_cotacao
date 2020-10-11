#___________________________________________________________________
#   Nome:               Extrator de cotação - Google
#   Desenvolvido por:   João Gabriel - @brjoaogabriel
#   Data da últ. att.:  11/10/2020
#   Data da criação:    10/10/2020
#___________________________________________________________________

#       DESCRIÇÃO DAS BIBLIOTECAS
#___________________________________________________________________
#   webdriver       > automação web
#   time            > esperar carregamento da página
from selenium import webdriver
import time

# Exemplo de link da cotação:    https://www.google.com/search?source=hp&ei=4UmBX97iA8DB5OUPzPWAiA8&q=BBDC4F&oq=BBDC4F&gs_lcp=CgZwc3ktYWIQAzIKCAAQsQMQRhD6ATIFCAAQsQMyBQgAELEDMgIIADICCAAyAggAMgIIADICCAAyAggAMgIIADoCCC46BQguELEDOgQIABAKOgkIABANEEYQ-gE6BAgAEA06BggAEA0QCjoGCAAQDRAeUIm5FFiMxxRg58cUaANwAHgAgAHkAYgBkQeSAQUyLjQuMZgBAKABAaoBB2d3cy13aXo&sclient=psy-ab&ved=0ahUKEwie17nMqKnsAhXAILkGHcw6APEQ4dUDCAY&uact=5

#   Responsável por gerar o link que leva até a api do googlee que apresenta informações sobre cotação e valuation de ativos listados na B3
#   Retorna o link que leva até as informações do ativo
def __Gera_Link_Cotacao(ativo):
    return f"https://www.google.com/search?source=hp&ei=4UmBX97iA8DB5OUPzPWAiA8&q={ativo}&oq={ativo}&gs_lcp=CgZwc3ktYWIQAzIKCAAQsQMQRhD6ATIFCAAQsQMyBQgAELEDMgIIADICCAAyAggAMgIIADICCAAyAggAMgIIADoCCC46BQguELEDOgQIABAKOgkIABANEEYQ-gE6BAgAEA06BggAEA0QCjoGCAAQDRAeUIm5FFiMxxRg58cUaANwAHgAgAHkAYgBkQeSAQUyLjQuMZgBAKABAaoBB2d3cy13aXo&sclient=psy-ab&ved=0ahUKEwie17nMqKnsAhXAILkGHcw6APEQ4dUDCAY&uact=5"

#   Responsável por entrar na api do google e extrair as informações
#   Retorna um dicionário contendo as principais informações da ação
def Pesquisa_Cotacao(tempo_espera, ativos):

    #   Cria variável que vai armazenar todos os dicionários
    print("Preparando a variável Cotacoes...")
    Cotacoes = []
    
    #   Cria manipulador da web
    print("Preparando a variável browser...")
    browser = webdriver.Firefox()

    #   Itera todos os ativos solicitados pelo usuário
    print("Começando a iteração dos ativos...")
    for ativo in ativos:

        #   Visitando o site
        print(f"Indo para o site do ativo: {ativo}")
        browser.get(__Gera_Link_Cotacao(ativo))

        print("Iniciando tempo de espera...")
        time.sleep(tempo_espera)

        #   Capturando os valores diários
        #   Nome do ativo
        print("Criando o dicionário que comportará os valores")
        Dicionario = {}
        
        Dicionario['Nome'] = ativo
        print(f"Nome do ativo: {Dicionario['Nome']}")

        Dicionario['Ativo'] = browser.find_element_by_class_name('HfMth').text
        Dicionario['Ativo'] = Dicionario['Ativo'].replace('BVMF: I', '').replace('NYSE: ','').replace('NASDAQ: ','').replace('BVMF: ','')
        print(f"Código do ativo: {Dicionario['Ativo']}")

        #   Informações diárias do ativo
        cotacao_atual = browser.find_element_by_class_name('N9cLBc').find_element_by_tag_name('span').text.split(" ")
        Dicionario['Cotacao'] = cotacao_atual[0].replace('.','').replace(',','.')
        Dicionario['Moeda'] = cotacao_atual[1]
        print(f"Valor do ativo: {cotacao_atual[0]}")
        print(f"Moeda do ativo: {cotacao_atual[1]}")
        cotacao_atual = None

        nome_campos = browser.find_elements_by_class_name('JgXcPd')
        valor_campos = browser.find_elements_by_class_name('iyjjgb')

        #   Transforma os valores para o formado americano
        for i in range(0, len(nome_campos),1):
            Dicionario[nome_campos[i].text] = valor_campos[i].text.replace('.','').replace(',','.').replace(' bi', '').replace(' mi', '')
            print(f"{nome_campos[i].text}: {Dicionario[nome_campos[i].text]}")

        #   Adiciona o dicionario ao retorno e destrói a variável
        print("Adicionando dicionario a lista...")
        Cotacoes.append(Dicionario)

        print("Destruindo dicionário...")
        Dicionario = None
        print()

    #   Finalizando
    print("Finalizando o browser...")
    browser.quit()
    print()

    return Cotacoes