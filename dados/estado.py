CARDAPIO=[]
MESAS=[]
ATENDENTES=[]
PEDIDOS=[]
PAGAMENTOS=[]
CONTADORES={"prato":1,"mesa":1,"atendente":1,"pedido":1,"item":1,"pagamento":1}

def proximo_id(tipo):
    valor=CONTADORES[tipo]; CONTADORES[tipo]+=1; return valor

def reiniciar_dados():
    for lista in (CARDAPIO,MESAS,ATENDENTES,PEDIDOS,PAGAMENTOS): lista.clear()
    for chave in CONTADORES: CONTADORES[chave]=1
