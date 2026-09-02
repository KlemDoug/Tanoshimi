mesas = {
        1: {
        "status": "Livre",
        "garcom": None,
        "pedido": None
        },
        2: {
        "status": "Ocupada",
        "garcom": None,
        "pedido": None
        },
        3: {
        "status": "Ocupada",
        "garcom": "Carlos",
        "pedido": None
        },
        4: {
        "status": "Ocupada",
        "garcom": "Ana",
        "pedido": {
        "itens": ["Pizza", "Refrigerante"],
        "valor": 85.00
            }
    }
}

def consultar_mesa(mesas):
    numero_mesa = int(input("Digite o número da mesa que deseja consultar: "))

    # confirmando se a mesa existe
    if numero_mesa not in mesas:
        print("Mesa não encontrada.")
        return

    mesa = mesas[numero_mesa]

    # consultando status da mesa
    if mesa["status"] != "Ocupada":
        print(f"Mesa {numero_mesa} não está ocupada. Status atual: {mesa['status']}")
        return

    # consultando se existe garçom responsável
    if mesa["garcom"] is None:
        print(f"Mesa {numero_mesa} ocupada, mas sem garçom vinculado.")
        return

    # consultando se existe pedido vinculado à mesa
    if mesa["pedido"] is None:
        print(f"Mesa {numero_mesa} atendida por {mesa["garcom"]}, mas ainda sem pedido registrado. ")
        return

    # enviando para a cozinha
    print(f"Mesa {numero_mesa} pronta: Pedido de atendente {mesa["garcom"]} encaminhado para cozinha.")
    mesas[numero_mesa] = {
        "pedido": {
        "numero_mesa": numero_mesa,
        "itens": "pedido",
        "garcom": "garcom"
            }
        }

consulta = consultar_mesa(mesas)
print(consulta)