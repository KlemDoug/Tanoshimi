def adicionar_item_pedido(pedido, prato, quantidade, observacoes=""):
    """
    Adiciona um item (prato, quantidade e observações) a um pedido existente.
    
    Parâmetros:
        pedido (dict): Dicionário contendo os dados do pedido atual.
        prato (dict): Dicionário contendo os dados do prato vindo do cardápio.
        quantidade (int): Quantidade solicitada do prato.
        observacoes (str, opcional): Observações adicionais para o preparo (ex: "sem cebola").
        
    Retorna:
        dict: O pedido atualizado com o novo item adicionado.
    """
    try:
        # Validação de parâmetros básicos
        if not isinstance(pedido, dict) or not isinstance(prato, dict):
            raise ValueError("O pedido e o prato devem ser informados em formato de dicionário.")
        
        if not isinstance(quantidade, int) or quantidade <= 0:
            raise ValueError("A quantidade deve ser um número inteiro maior que zero.")
        
        # Verifica se o prato está disponível (integrado ao cardápio)
        if not prato.get("disponivel", True):
            raise ValueError(f"O prato '{prato.get('nome', 'Desconhecido')}' não está disponível no momento.")
        
        # Garante que a estrutura de itens do pedido existe
        if "itens" not in pedido:
            pedido["itens"] = []
            
        # Cria o objeto do item do pedido
        novo_item = {
            "codigo_prato": prato.get("codigo"),
            "nome_prato": prato.get("nome"),
            "preco_unitario": prato.get("preco", 0.0),
            "quantidade": quantidade,
            "observacoes": observacoes,
            "subtotal": prato.get("preco", 0.0) * quantidade
        }
        
        # Adiciona o item à lista do pedido
        pedido["itens"].append(novo_item)
        
        print(f"Sucesso: {quantidade}x '{prato.get('nome')}' adicionado(s) ao pedido.")
        return pedido

    except Exception as e:
        print(f"Erro ao adicionar item ao pedido: {e}")
   