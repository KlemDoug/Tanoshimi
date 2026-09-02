from dados import MESAS,proximo_id
STATUS={"livre","ocupada","reservada","aguardando_pagamento"}

def cadastrar_mesa(numero,capacidade):
    if numero<=0 or capacidade<=0: raise ValueError("Valores inválidos.")
    m={"id":proximo_id("mesa"),"numero":numero,"capacidade":capacidade,"status":"livre","atendente_id":None}; MESAS.append(m); return m

def consultar_mesa(valor):
    for m in MESAS:
        if m["id"]==valor or m["numero"]==valor: return m
    raise LookupError("Mesa não encontrada.")

def listar_mesas(status=None):
    if not MESAS:
        for n,c in ((1,2),(2,4),(3,4),(4,6),(5,8),(6,2)): cadastrar_mesa(n,c)
    if status and status not in STATUS: raise ValueError("Status inválido.")
    return [m for m in MESAS if not status or m["status"]==status]

def alterar_status_mesa(mesa_id,status):
    if status not in STATUS: raise ValueError("Status inválido.")
    m=consultar_mesa(mesa_id); m["status"]=status; return m

def vincular_atendente_mesa(mesa_id,atendente_id):
    from funcoes.atendentes import consultar_atendente
    m=consultar_mesa(mesa_id); consultar_atendente(atendente_id); m["atendente_id"]=atendente_id; return m
