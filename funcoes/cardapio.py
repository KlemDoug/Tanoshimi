from dados import CARDAPIO,proximo_id

def cadastrar_prato(nome,descricao,preco,categoria,disponivel=True):
    if not nome.strip() or not descricao.strip() or not categoria.strip(): raise ValueError("Campos obrigatórios.")
    if preco<0: raise ValueError("Preço inválido.")
    prato={"id":proximo_id("prato"),"nome":nome.strip(),"descricao":descricao.strip(),"preco":round(float(preco),2),"categoria":categoria.strip(),"disponivel":bool(disponivel)}
    CARDAPIO.append(prato); return prato

def consultar_prato(valor):
    for p in CARDAPIO:
        if p["id"]==valor or p["nome"].lower()==str(valor).lower(): return p
    raise LookupError("Prato não encontrado.")

def listar_cardapio(apenas_disponiveis=True):
    if not CARDAPIO:
        cadastrar_prato("Temaki de salmão","Cone de alga, arroz e salmão",32.90,"Temakis")
        cadastrar_prato("Hot roll","Sushi empanado servido quente",28.00,"Sushis")
        cadastrar_prato("Yakisoba de legumes","Macarrão oriental com legumes",35.50,"Pratos quentes")
        cadastrar_prato("Guioza","Pastel oriental grelhado",24.00,"Entradas")
        cadastrar_prato("Chá verde","Chá verde servido quente",9.00,"Bebidas")
    return [p for p in CARDAPIO if p["disponivel"] or not apenas_disponiveis]

def atualizar_prato(prato_id,nome=None,descricao=None,preco=None,categoria=None):
    p=consultar_prato(prato_id)
    if nome: p["nome"]=nome.strip()
    if descricao: p["descricao"]=descricao.strip()
    if preco is not None:
        if preco<0: raise ValueError("Preço inválido.")
        p["preco"]=round(float(preco),2)
    if categoria: p["categoria"]=categoria.strip()
    return p

def alterar_disponibilidade_prato(prato_id,disponivel):
    p=consultar_prato(prato_id); p["disponivel"]=bool(disponivel); return p
