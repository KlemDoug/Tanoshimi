from dados import garcons, pedidos

def alterar_status_garcom(id_garcom, novo_status):
    if novo_status not in ['disponivel', 'ocupado']:
        return f"ERRO: Status '{novo_status}' inválido! Use disponivel ou ocupado"
    
    if id_garcom not in garcons:
        return f"ERRO: Garçom com ID {id_garcom} não encontrado!"
    
    nome = garcons[id_garcom]['nome']
    status_atual = garcons[id_garcom]['status']
    
    if status_atual == novo_status:
        return f"Garçom {nome} já está com status '{novo_status}'."
    
    if novo_status == 'ocupado':
        pedidos_abertos = 0
        for pedido in pedidos.values():
            if pedido['id_garcom'] == id_garcom and pedido['status'] in ['aberto', 'enviado_cozinha', 'preparando']:
                pedidos_abertos += 1
        
        if pedidos_abertos > 0:
            return f"ERRO: Garçom {nome} tem {pedidos_abertos} pedido(s) em aberto. Finalize ou repasse os pedidos antes de alterar o status."
    
    garcons[id_garcom]['status'] = novo_status
    return f"Status do garçom {nome} alterado de '{status_atual}' para '{novo_status}' com sucesso!"