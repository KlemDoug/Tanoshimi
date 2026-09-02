from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from dados import reiniciar_dados
from funcoes import *
reiniciar_dados(); c=listar_cardapio(); m=listar_mesas(); a=listar_atendentes(); p=criar_pedido(m[0]["id"],a[0]["id"]); i=adicionar_item_pedido(p["id"],c[0]["id"],2); n=gerar_numero_pedido(p["id"]); enviar_pedido_cozinha(p["id"]); atualizar_preparo_item(i["id"],"entregue"); registrar_pagamento(p["id"],calcular_total_pedido(p["id"]),"PIX"); fechar_conta(p["id"]); assert p["status"]=="pago" and m[0]["status"]=="livre"; print("OK",n)
