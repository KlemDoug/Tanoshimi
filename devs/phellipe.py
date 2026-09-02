
def listar_pedidos_da_mesa(numero_mesa: int, pedidos: list[dict], status: str | None = None, exibir: bool = True) -> list[dict]:
    '''
    Apresenta e retorna todos os pedidos associados a uma mesa e, opcionalmente, apresenta-os no terminal.

    Args:
        numero_mesa: Número identificador da mesa.
        pedidos: Lista de dicionários representando os pedidos.
        status: Status opcional usado para filtrar os pedidos.
        exibir: Indica se os pedidos encontrados devem ser exibidos no terminal. O padrão é True.

    Returns:
        Lista de pedidos associados à mesa e ao status informado.
        Retorna uma lista vazia quando nenhum pedido é encontrado.

    Raises:
        TypeError: Se os parâmetros tiverem tipos inadequados.
        ValueError: Se o número da mesa não for maior que zero.
    '''

    LARGURA_EXIBICAO = 100

    # Validações
    if not isinstance(numero_mesa, int):
        raise TypeError(
            "Parâmetro inválido: o número da mesa deve ser um número inteiro.")

    if numero_mesa <= 0:
        raise ValueError(
            "Parâmetro inválido: o número da mesa deve ser maior que zero.")

    if not isinstance(pedidos, list):
        raise TypeError(
            "Parâmetro inválido: os pedidos devem ser fornecidos em uma lista.")

    if status is not None and not isinstance(status, str):
        raise TypeError(
            "Parâmetro inválido: o status deve ser uma string ou None.")

    if not isinstance(exibir, bool):
        raise TypeError(
            "Parâmetro inválido: exibir deve ser um valor booleano.")

    # Lógica da função
    pedidos_da_mesa = []

    for pedido in pedidos:
        if pedido['numero_mesa'] == numero_mesa:

            if status is not None:
                if pedido['status'].lower() == status.lower():
                    pedidos_da_mesa.append(pedido)
            else:
                pedidos_da_mesa.append(pedido)

    if not exibir:
        return pedidos_da_mesa

    # Exibição no terminal
    print("=" * LARGURA_EXIBICAO)
    print("RESTAURANTE TANOSHIMI - VISÃO DO GARÇOM".center(LARGURA_EXIBICAO))
    print("=" * LARGURA_EXIBICAO)

    if status is not None:
        print(
            f"PEDIDOS DA MESA {numero_mesa} - STATUS: {status.upper()}".center(LARGURA_EXIBICAO))
    else:
        print(f"PEDIDOS DA MESA {numero_mesa}".center(LARGURA_EXIBICAO))

    print("=" * LARGURA_EXIBICAO)

    if not pedidos_da_mesa:

        if status is None:
            mensagem = "Nenhum pedido foi encontrado para essa mesa."
        else:
            mensagem = f"Nenhum pedido com status '{status.lower()}' foi encontrado para essa mesa."

        print(mensagem.center(LARGURA_EXIBICAO))

    for indice_pedido, pedido in enumerate(pedidos_da_mesa):
        if indice_pedido != 0:
            print("=" * LARGURA_EXIBICAO)

        print(
            f"PEDIDO {pedido['numero_pedido']} ({pedido['status']})".center(LARGURA_EXIBICAO))
        print("=" * LARGURA_EXIBICAO)

        itens = pedido['itens']

        if itens:
            for indice_item, item in enumerate(itens, start=1):
                codigo_prato = item["codigo_prato"]
                nome_prato = item['nome_prato']
                quantidade = item['quantidade']
                preco_unitario = item["preco_unitario"]
                subtotal = item["subtotal"]
                observacoes = item['observacoes']

                print(
                    f"{indice_item:02d} - {nome_prato:<25} | Qtd: {quantidade} | Unitário: R$ {preco_unitario:>7.2f} | Subtotal: R$ {subtotal:>7.2f}")

                print(" "*5 + f"Código do prato: {codigo_prato}")

                if observacoes:
                    print(" "*5 + f"Observações: {observacoes}")

                if indice_item != len(itens):
                    print("- " * (LARGURA_EXIBICAO // 2))
        else:
            print("Nenhum item foi adicionado ao pedido.".center(LARGURA_EXIBICAO))

    print("=" * LARGURA_EXIBICAO)

    return pedidos_da_mesa
