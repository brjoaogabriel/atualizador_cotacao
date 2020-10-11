#___________________________________________________________________
#   Nome:               Extrator de cotação - Google
#   Desenvolvido por:   João Gabriel - @brjoaogabriel
#   Data da últ. att.:  11/10/2020
#   Data da criação:    10/10/2020
#   Descrição:          Utilizado para solicitar uma lista para
#                           o usuário
#___________________________________________________________________

def Solicita_Ativos():
    __confirmacao = False

    __mensagem = """
    Olá, usuário!
    Liste os ativos que gostaria de extrair da cotação.
    Lembre, incluir um ativo que não está listado na api do google irá ocasionar em um erro

    Como fazer:
        Escreva os ativos que quer analisar até que esteja satisfeito, então, aperte ENTER com o campo vazio.
    """
    print(__mensagem)

    while __confirmacao == False:

        __ativos = []

        __entrada = "."
        while __entrada != "":
            __entrada = input("- ").strip().upper()
            if __entrada != "":
                __ativos.append(__entrada)

        if len(__ativos) > 0:
            __confirma = """
            Aperte ENTER para confirmar que deseja extrair os ativos abaixo ou escreva qualquer coisa e aperte ENTER para solicitar novamente:
            """
            print(__confirma)
            for __ativo in __ativos:
                print(f"- {__ativo}")

            if input().strip() == "":
                return __ativos
            else:
                print("OK, retornando para a solicitação de ativos...\n")
        
        else:
            __confirma = """
            Você não inseriu nenhum ativo, digite qualquer coisa caso deseje fechar o programa ou digite NÃO caso queira solicitar novamente
            """
            if input(__confirma) == "OK":
                exit()

    return __ativos