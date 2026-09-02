from dados import reiniciar_dados
from funcoes import *

def inteiro(msg):
    while True:
        try: return int(input(msg))
        except ValueError: print("Digite um número inteiro.")

def decimal(msg):
    while True:
        try: return float(input(msg).replace(",","."))
        except ValueError: print("Digite um valor numérico.")

def pausa(): input("\nENTER para continuar...")

def mostrar_cardapio():
    print("\n--- CARDÁPIO ---")
    for p in listar_cardapio(False): print(f"{p['id']} - {p['nome']} | R$ {p['preco']:.2f} | {'disponível' if p['disponivel'] else 'indisponível'}")

def mostrar_mesas():
    print("\n--- MESAS ---")
    for m in listar_mesas(): print(f"ID {m['id']} | Mesa {m['numero']} | {m['status']} | capacidade {m['capacidade']}")

def mostrar_atendentes():
    print("\n--- ATENDENTES ---")
    for a in listar_atendentes(False): print(f"ID {a['id']} | {a['nome']} | {a['status']}")

def menu_cardapio():
    while True:
        print("\n1 Listar | 2 Cadastrar | 3 Atualizar | 4 Disponibilidade | 0 Voltar")
        op=input("Opção: ")
        try:
            if op=="1": mostrar_cardapio(); pausa()
            elif op=="2": print(cadastrar_prato(input("Nome: "),input("Descrição: "),decimal("Preço: "),input("Categoria: "))); pausa()
            elif op=="3":
                mostrar_cardapio(); pid=inteiro("ID: "); p=consultar_prato(pid)
                nome=input(f"Nome [{p['nome']}]: ") or None; preco=input(f"Preço [{p['preco']}]: ")
                print(atualizar_prato(pid,nome=nome,preco=float(preco.replace(',','.')) if preco else None)); pausa()
            elif op=="4": mostrar_cardapio(); print(alterar_disponibilidade_prato(inteiro("ID: "),input("Disponível? S/N: ").lower()=="s")); pausa()
            elif op=="0": return
        except (ValueError,LookupError) as e: print("Erro:",e); pausa()

def menu_cadastros():
    while True:
        print("\n1 Listar mesas | 2 Cadastrar mesa | 3 Listar atendentes | 4 Cadastrar atendente | 5 Vincular | 0 Voltar")
        op=input("Opção: ")
        try:
            if op=="1": mostrar_mesas(); pausa()
            elif op=="2": print(cadastrar_mesa(inteiro("Número: "),inteiro("Capacidade: "))); pausa()
            elif op=="3": mostrar_atendentes(); pausa()
            elif op=="4": print(cadastrar_atendente(input("Nome: "),input("Matrícula: "))); pausa()
            elif op=="5": mostrar_mesas(); mostrar_atendentes(); print(vincular_atendente_mesa(inteiro("ID mesa: "),inteiro("ID atendente: "))); pausa()
            elif op=="0": return
        except (ValueError,LookupError) as e: print("Erro:",e); pausa()

def menu_pedidos():
    while True:
        print("\n1 Abrir | 2 Adicionar item | 3 Consultar | 4 Gerar número | 5 Cancelar | 0 Voltar")
        op=input("Opção: ")
        try:
            if op=="1": mostrar_mesas(); mostrar_atendentes(); print(criar_pedido(inteiro("ID mesa: "),inteiro("ID atendente: "))); pausa()
            elif op=="2": mostrar_cardapio(); print(adicionar_item_pedido(inteiro("ID pedido: "),inteiro("ID prato: "),inteiro("Quantidade: "),input("Observação: "))); pausa()
            elif op=="3":
                v=input("ID ou número: "); p=consultar_pedido(int(v) if v.isdigit() else v); print(p); print("Total: R$",calcular_total_pedido(p['id'])); pausa()
            elif op=="4": print(gerar_numero_pedido(inteiro("ID pedido: "))); pausa()
            elif op=="5": print(cancelar_pedido(inteiro("ID pedido: "),input("Motivo: "),input("Responsável: "))); pausa()
            elif op=="0": return
        except (ValueError,LookupError) as e: print("Erro:",e); pausa()

def menu_cozinha():
    while True:
        print("\n1 Enviar pedido | 2 Ver fila | 3 Atualizar item | 0 Voltar")
        op=input("Opção: ")
        try:
            if op=="1": pid=inteiro("ID pedido: "); gerar_numero_pedido(pid); print(enviar_pedido_cozinha(pid)); pausa()
            elif op=="2": print(*listar_fila_cozinha(),sep="\n"); pausa()
            elif op=="3": print(*listar_fila_cozinha(),sep="\n"); print(atualizar_preparo_item(inteiro("ID item: "),input("Status [recebido/em_preparo/pronto/entregue]: "))); pausa()
            elif op=="0": return
        except (ValueError,LookupError) as e: print("Erro:",e); pausa()

def menu_caixa():
    while True:
        print("\n1 Buscar e pagar | 2 Fechar conta | 0 Voltar")
        op=input("Opção: ")
        try:
            if op=="1":
                c=buscar_conta_por_numero(input("Número do pedido: ")); print(c)
                alterar_status_pedido(c["pedido_id"],"aguardando_pagamento"); print(registrar_pagamento(c["pedido_id"],decimal("Valor recebido: "),input("Meio: "))); pausa()
            elif op=="2": print(fechar_conta(inteiro("ID pedido: "))); pausa()
            elif op=="0": return
        except (ValueError,LookupError) as e: print("Erro:",e); pausa()

def executar_sistema():
    reiniciar_dados(); listar_cardapio(); listar_mesas(); listar_atendentes()
    while True:
        print("\n=== TANOSHIMI ===\n1 Cardápio\n2 Mesas e atendentes\n3 Pedidos\n4 Cozinha\n5 Caixa\n0 Sair")
        op=input("Opção: ")
        if op=="1": menu_cardapio()
        elif op=="2": menu_cadastros()
        elif op=="3": menu_pedidos()
        elif op=="4": menu_cozinha()
        elif op=="5": menu_caixa()
        elif op=="0": print("Sistema encerrado."); break
        else: print("Opção inválida.")

if __name__=="__main__": executar_sistema()
