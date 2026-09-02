# função consultar_pedido_python_ver1.2()
# foram feitos melhorias nessa versão

'''
para funcionar vou precisar importar funções externas, por exemplo:
from adicionar_pedido import adicionar_pedido
from remover_pedido import remover_pedido
from cancelar_pedido import cancelar_pedido
'''
# criação de uma lista "falsa" para testes:::::
# ----------------------------------------------BLOCO DE TESTES------------------------------------
lista_pedidos = [
    {
        "numero_pedido": 20,
        "mesa": 4,
        "status": "PREPARANDO",
        "pagamento": "PENDENTE",
        "garcom": "José",
        "valor_total": 105.98
    },
    {
        "numero_pedido": 21,
        "mesa": 7,
        "status": "PRONTO",
        "pagamento": "PENDENTE",
        "garcom": "Cleiton",
        "valor_total": 75.90
    },
    {
        "numero_pedido": 22,
        "mesa": 14,
        "status": "ABERTO",
        "pagamento": "PENDENTE",
        "garcom": "José",
        "valor_total": 123.50
    }
]

# Funções para testes

def remover_item(pedido):
    print(
        f"\nUm item seria removido do "
        f"pedido nº {pedido['numero_pedido']}."
    )

def adicionar_item(pedido):
    print(
        f"\nUm item seria adicionado ao "
        f"pedido nº {pedido['numero_pedido']}."
    )

def cancelar_pedido(pedido):
    pedido["status"] = "CANCELADO"

    print(
        f"\nO pedido nº {pedido['numero_pedido']} "
        "foi cancelado."
    )
# --------------------------------------FIM DO BLOCO DE TESTES --------------------------------------------------


def procurar_pedido(numero_digitado, lista_pedidos):
    '''
    FUNÇÃO AUXILIAR
     Função que procura o pedido dentro da lista de pedido
    (essa lista pode ter sido criada quando a função "criar_pedido()" é executada,
    esta função recebe o nº digitado e a lista criada como parâmetros
    se encontrar a lista vazia, retornará "nada", se não encontrar o valor,
    retornará que o pedido não existe, se encontrar um pedido equivalente ao número registrado,
    retornará o pedido
   '''
    for pedido in lista_pedidos:  # ercorre a lista em busca do pedido numero_pedido é o numero que foi associado lá na criação
        if pedido["numero_pedido"] == numero_digitado:# retorna os dados equivalente a este pedido
            return pedido
    
    return None # aqui caso não encontre ele precisa retornar uma "resposta" negativa (no caso vazia)


def mostrar_pedido(pedido):
    '''
    FUNÇÃO AUXILIAR
    Mostra os dados do pedido encontrado.
    '''
    valor_formatado = f"{pedido['valor_total']:.2f}"

    print("\n====================================")
    print(f"PEDIDO Nº {pedido['numero_pedido']}")
    print("====================================")
    print(f"Mesa: {pedido['mesa']}")
    print(f"Garçom: {pedido['garcom']}")
    print(f"Status: {pedido['status']}")
    print(f"Pagamento: {pedido['pagamento']}")
    print(f"\nValor total: R$ {valor_formatado}")
    print("====================================")


def consultar_pedido(lista_pedidos):
    '''
    Função principal da consulta.
    executa as duas funções auxiliares:
    Solicita o número, procura o pedido e mostra seus dados.
    Retorna o pedido encontrado ou None.
    '''

    if len(lista_pedidos) == 0:  # verificar se tem algum pedido na lista
        print("\nNão existem pedidos cadastrados.")
        return None

    pedido_encontrado = None # aqui o pedido inicia vazio, só passará a ter valor quando a função for executada no while

    continuar_consulta = "s" # define o valor para o while iniciar o loop
    while continuar_consulta == "s":
        try:
            '''
            ENTENDENDO A LINHA DE BAIXO:
            pega a informação do usuário(input)
            salva em numero_digitado
            em seguida executa a função de consulta baseada no numero digitado
            armazena dentro da variavel pedido_encontrado
            '''
            numero_digitado = int(input("\nDigite o número do pedido que deseja consultar: "))
            pedido_encontrado = procurar_pedido(numero_digitado,lista_pedidos)

            if pedido_encontrado is None:# se não tiver nada na lista ou não encontrar o nº de pedido,ele ainda vai estar como None
                print(
                    f"\nO pedido nº {numero_digitado} não foi encontrado.")
                
            else:#se achar, ele puxa lá da variável que armazenou a execução da função com o numero_digitado
                mostrar_pedido(pedido_encontrado)

            '''
            ENTENDENDO A LINHA ABAIXO:
            essa linha lê a resposta do usuário para continuar
            consultando ou não
            '''
            continuar_consulta = input("\nDeseja realizar outra consulta? (s/n): \n").lower()  # lower para colocar em minusculo

            # valida se foi digitado s ou n:
            while (continuar_consulta != "s" and continuar_consulta != "n"):
                print("\nResposta inválida.")
                continuar_consulta = input("Digite apenas s ou n: ").lower()
        except ValueError:
            print("\nEntrada inválida. Digite somente números.")

    # Verifica se existe um pedido para poder dar opções ao usuário
    if pedido_encontrado != None:
        print("\n=========================================")
        print("Tecle 1 para: Adicionar mais itens")
        print("Tecle 2 para: Remover itens")
        print("Tecle 3 para: Continuar com o pedido atual")
        print("Tecle 4 para: Cancelar o pedido")
        print("Tecle 0 para: Sair")
        print("=========================================")

        opcao = input("\nComo deseja prosseguir? ")  # salva a resposta em opcao

        match opcao: # aqui entra a ligação com as demais funções
            case "1":
                adicionar_item(pedido_encontrado)
            case "2":
                remover_item(pedido_encontrado)
            case "3":
                print(f"\nO pedido nº {pedido_encontrado['numero_pedido']} continuará sem alterações.")
            case "4":
                cancelar_pedido(pedido_encontrado)
            case "0":
                print("\nSaindo da consulta")
            case _:
                print("\nOpção inválida.")
    else:
        print("\nPedido Inexistente") #se não tem um pedido diferente de None significa que não tem pedidos com essa numeração variável pedido_encontrado ainda possui valor "vazio"
    return pedido_encontrado


# CHAMAR A FUNÇÃO PARA TESTAR:::
consultar_pedido(lista_pedidos)