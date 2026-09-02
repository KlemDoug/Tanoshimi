from dados import ATENDENTES,MESAS,proximo_id
STATUS={"disponível","atendendo","fora_do_turno"}

def cadastrar_atendente(nome,matricula,status="disponível"):
    if not nome.strip() or not matricula.strip(): raise ValueError("Nome e matrícula obrigatórios.")
    if status not in STATUS: raise ValueError("Status inválido.")
    a={"id":proximo_id("atendente"),"nome":nome.strip(),"matricula":matricula.strip(),"status":status}; ATENDENTES.append(a); return a

def consultar_atendente(valor):
    for a in ATENDENTES:
        if a["id"]==valor or a["matricula"]==str(valor): return a
    raise LookupError("Atendente não encontrado.")

def listar_atendentes(apenas_ativos=True):
    if not ATENDENTES:
        cadastrar_atendente("Akira Santos","A001"); cadastrar_atendente("Bianca Lima","A002"); cadastrar_atendente("Carlos Nunes","A003","fora_do_turno")
    return [a for a in ATENDENTES if not apenas_ativos or a["status"]!="fora_do_turno"]

def alterar_status_atendente(atendente_id,status):
    if status not in STATUS: raise ValueError("Status inválido.")
    a=consultar_atendente(atendente_id); a["status"]=status; return a

def listar_mesas_do_atendente(atendente_id):
    consultar_atendente(atendente_id); return [m for m in MESAS if m["atendente_id"]==atendente_id]
