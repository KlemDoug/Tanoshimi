from dados import PAGAMENTOS,proximo_id
from funcoes.pedidos import consultar_pedido,calcular_total_pedido,alterar_status_pedido
from funcoes.mesas import alterar_status_mesa

def gerar_numero_pedido(pedido_id):
    p=consultar_pedido(pedido_id)
    if not p["numero"]: p["numero"]=f"TAN-{p['id']:05d}"
    return p["numero"]

def buscar_conta_por_numero(numero):
    p=consultar_pedido(numero); return {"pedido_id":p["id"],"numero":p["numero"],"mesa_id":p["mesa_id"],"itens":p["itens"],"total":calcular_total_pedido(p["id"]),"status":p["status"]}

def registrar_pagamento(pedido_id,valor,meio):
    p=consultar_pedido(pedido_id); total=calcular_total_pedido(pedido_id)
    if p["status"] in {"pago","cancelado"} or valor<total: raise ValueError("Pedido encerrado ou valor insuficiente.")
    pag={"id":proximo_id("pagamento"),"pedido_id":pedido_id,"valor":round(float(valor),2),"meio":meio.strip(),"troco":round(valor-total,2),"status":"confirmado"}; PAGAMENTOS.append(pag); return pag

def fechar_conta(pedido_id):
    p=consultar_pedido(pedido_id)
    if not any(x["pedido_id"]==pedido_id and x["status"]=="confirmado" for x in PAGAMENTOS): raise ValueError("Pagamento não confirmado.")
    alterar_status_pedido(pedido_id,"pago"); alterar_status_mesa(p["mesa_id"],"livre"); return p
