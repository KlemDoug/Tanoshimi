# FECHAMENTO DA CONTA

numero_da_mesa = numero_da_mesa
numero_pedido = numero_pedido
valor_total = valor_total

if registrar_pagamento True
try:
    print(f"Mesa número: {numero_da_mesa}, pedido número:{numero_pedido}, valor_pago{valor_total}) #visão REST
    
    novo_pedido = input("Você deseja acrescentar algo ao seu pedido? Digite SIM, caso deseje e NÃO para encerrar sua conta:") #visão CLI
Except


finally:
    print(Obrigada por escolher o Restaurante XXX. Esperamos qie volte o mais breve possível!)

if novo_pedido =="SIM":
    return listar_cardapio #visão CLI

else:
    print(f"Fechando o seu pedido e gerando o valor total à pagar...:")
    print({valor_consumido})

valor_consumido = float(input("Digite o valor consumido: R$ "))
pagamento = input("A conta foi paga? (S/N): ")

if pagamento == "S":
    print(f"Pedido {numero_pedido} no valor de R$ {valor_consumido:.2f} foi pago.")
    print("Conta fechada com sucesso!")
    print(f"Mesa {numero_mesa} liberada.")
else:
    print(f"Pedido {numero_pedido} no valor de R$ {valor_consumido: 2f}está pendente de pagamento.")
