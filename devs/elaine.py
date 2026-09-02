#(Consultar_pratos)


# Loop principal da consulta
rodando = True

while rodando:
    print("--- CONSULTA DE PRATOS ---")
    busca = input("Digite o CÓDIGO ou o NOME do prato: ").strip().lower()
    
    if busca == "sair":
        rodando = False
    else:
        encontrado = False
        
        # Percorre o cardápio procurando pelo código ou pelo nome
        for prato in cardapio:
            if busca == prato["codigo"] or busca == prato["nome"]:
               
                print(f"Código: {prato['codigo']}")
                print(f"Nome: {prato['nome'].capitalize()}")
                print(f"Preço: R$ {prato['preco']:.2f}\n")
                encontrado = True
                break  # Para a busca assim que encontra
        
        if not encontrado:
            print("\nPrato não encontrado. Verifique o nome ou código e tente novamente.\n")



#Como funciona:

#input e lower, permite que o cliente digite o nome em maiúsculas ou minúsculas sem gerar erro na busca

#O comando if busca == prato["codigo"] or busca == prato["nome"] verifica se a entrada do usuário combina com o número ou com o nome do item.

#Loop while, mantém o cardápio ativo para várias consultas até que o usuário digite "sair".
