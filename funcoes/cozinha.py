from dados import PEDIDOS
from funcoes.pedidos import consultar_pedido,alterar_status_pedido
STATUS={"recebido","em_preparo","pronto","entregue"}

def enviar_pedido_cozinha(pedido_id):
    p=consultar_pedido(pedido_id)
    if p["status"]!="aberto": raise ValueError("Somente pedidos abertos podem ser enviados.")
    if not p["itens"]: raise ValueError("Pedido sem itens.")
    p["status"]="enviado"
    for i in p["itens"]: i["status_preparo"]="recebido"
    return p

def listar_fila_cozinha():
    fila=[]
    for p in PEDIDOS:
        if p["status"] in {"enviado","em_preparo","pronto"}:
            for i in p["itens"]:
                if i["status_preparo"]!="entregue": fila.append({"item_id":i["id"],"pedido_id":p["id"],"numero":p["numero"],"prato":i["prato"],"quantidade":i["quantidade"],"status":i["status_preparo"]})
    return fila

def atualizar_preparo_item(item_id,status):
    if status not in STATUS: raise ValueError("Status inválido.")
    for p in PEDIDOS:
        for i in p["itens"]:
            if i["id"]==item_id:
                i["status_preparo"]=status; estados=[x["status_preparo"] for x in p["itens"]]
                if all(x=="entregue" for x in estados): alterar_status_pedido(p["id"],"entregue")
                elif all(x in {"pronto","entregue"} for x in estados): alterar_status_pedido(p["id"],"pronto")
                elif any(x=="em_preparo" for x in estados): alterar_status_pedido(p["id"],"em_preparo")
                return i
    raise LookupError("Item não encontrado.")
