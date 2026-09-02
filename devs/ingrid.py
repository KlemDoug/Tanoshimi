pedidos = []


def criar_pedido(numero_pedido, numero_mesa, id_garcom):
    # Verifica se já existe um pedido com esse número
    for pedido in pedidos:
        if pedido["numero_pedido"] == numero_pedido:
            print("Erro: esse número de pedido já existe.")
            return None

    # Cria o novo pedido
    novo_pedido = {
        "numero_pedido": numero_pedido,
        "numero_mesa": numero_mesa,
        "id_garcom": id_garcom,
        "itens": [],
        "status": "Aberto"
    }

    # Adiciona o pedido à lista
    pedidos.append(novo_pedido)

    print("Pedido criado com sucesso!")

    return novo_pedido
