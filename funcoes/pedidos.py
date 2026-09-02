from dados import PEDIDOS,proximo_id
from funcoes.cardapio import consultar_prato
from funcoes.mesas import consultar_mesa,alterar_status_mesa
from funcoes.atendentes import consultar_atendente
STATUS={"aberto","enviado","em_preparo","pronto","entregue","aguardando_pagamento","pago","cancelado"}

def criar_pedido(mesa_id,atendente_id):
    m=consultar_mesa(mesa_id); consultar_atendente(atendente_id)
    if m["status"] not in {"livre","ocupada"}: raise ValueError("Mesa indisponível.")
    p={"id":proximo_id("pedido"),"numero":None,"mesa_id":mesa_id,"atendente_id":atendente_id,"status":"aberto","itens":[],"motivo_cancelamento":None}
    PEDIDOS.append(p); m["atendente_id"]=atendente_id; alterar_status_mesa(mesa_id,"ocupada"); return p

def adicionar_item_pedido(pedido_id,prato_id,quantidade,observacao=""):
    p=consultar_pedido(pedido_id); prato=consultar_prato(prato_id)
    if p["status"]!="aberto": raise ValueError("Pedido não está aberto.")
    if not prato["disponivel"] or quantidade<=0: raise ValueError("Item indisponível ou quantidade inválida.")
    i={"id":proximo_id("item"),"prato_id":prato_id,"prato":prato["nome"],"quantidade":quantidade,"preco_unitario":prato["preco"],"observacao":observacao.strip(),"status_preparo":"aguardando"}; p["itens"].append(i); return i

def remover_item_pedido(pedido_id,item_id,quantidade=None):
    p=consultar_pedido(pedido_id)
    if p["status"]!="aberto": raise ValueError("Pedido não pode ser alterado.")
    for i in p["itens"]:
        if i["id"]==item_id:
            if quantidade is None or quantidade>=i["quantidade"]: p["itens"].remove(i); return None
            if quantidade<=0: raise ValueError("Quantidade inválida.")
            i["quantidade"]-=quantidade; return i
    raise LookupError("Item não encontrado.")

def consultar_pedido(valor):
    for p in PEDIDOS:
        if p["id"]==valor or p["numero"]==valor: return p
    raise LookupError("Pedido não encontrado.")

def calcular_total_pedido(pedido_id):
    return round(sum(i["quantidade"]*i["preco_unitario"] for i in consultar_pedido(pedido_id)["itens"]),2)

def alterar_status_pedido(pedido_id,status):
    if status not in STATUS: raise ValueError("Status inválido.")
    p=consultar_pedido(pedido_id); p["status"]=status; return p

def cancelar_pedido(pedido_id,motivo,responsavel):
    p=consultar_pedido(pedido_id)
    if p["status"]=="pago": raise ValueError("Pedido pago não pode ser cancelado.")
    p["status"]="cancelado"; p["motivo_cancelamento"]=motivo.strip(); p["cancelado_por"]=responsavel.strip(); alterar_status_mesa(p["mesa_id"],"livre"); return p

def listar_pedidos_da_mesa(mesa_id,incluir_encerrados=False):
    consultar_mesa(mesa_id); return [p for p in PEDIDOS if p["mesa_id"]==mesa_id and (incluir_encerrados or p["status"] not in {"pago","cancelado"})]
