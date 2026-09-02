def  atualizar_preparo_item(nome:str,quantidade: int = 1,prato:bool = False) -> dict:
    """Atualiza o preparo de um item"""
    try:
        if not isinstance(nome,str) or not nome.strip():
            raise ValueError("Nome inválido")

        if not isinstance(quantidade,int) or quantidade <=0:
            raise ValueError("Quantidade deve ser maior que zero")

        if not isinstance(prato,bool):
            raise ValueError("Prato deve ser booleano")
        
        item_atualizado = {
            "nome":nome,
            "quantidade":quantidade,
            "prato":prato
        }

        return item_atualizado


    except Exception as e:
        print(e)
        return {
        "nome":None,
        "quantidade":None,
        "prato":None
    }
    

    
