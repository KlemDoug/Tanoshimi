#Projeto restaurante Tanoshimi - Sistema de Atendimento

#Função atualizar_prato()
#Altera os dados comerciais e descritivos do prato.


cardapio = [
    {"id": 1, "nome": "Sushi de Salmão", "preco": 28.00, "descricao": "Combinado com 8 peças", "disponivel": True},
    {"id": 2, "nome": "Temaki de Atum", "preco": 22.00, "descricao": "Cone de alga com atum e cream cheese", "disponivel": True},
    {"id": 3, "nome": "Yakisoba", "preco": 32.00, "descricao": "Macarrão oriental com legumes e carne", "disponivel": True},
    {"id": 4, "nome": "Tempurá de Camarão", "preco": 38.00, "descricao": "Camarões empanados fritos", "disponivel": True},
    {"id": 5, "nome": "Missoshiru", "preco": 12.00, "descricao": "Sopa de missô tradicional", "disponivel": True},
]

def atualizar_prato(menu):
    id_prato = int(input("Digite o ID do prato que deseja atualizar: "))  #Busca o prato pelo ID fornecido pelo usuário
    prato_encontrado = None    #Inicializa a variável para armazenar o prato encontrado

    for prato in menu:  #Itera sobre cada prato no cardápio
        if prato["id"] == id_prato:   #Verifica se o ID do prato atual corresponde ao ID fornecido pelo usuário
            prato_encontrado = prato     #Armazena o prato encontrado na variável prato_encontrado
            break

    if prato_encontrado:
        print(f"Prato encontrado: {prato_encontrado['nome']}")   #Exibe o nome do prato encontrado
        novo_nome = input("Digite o novo nome do prato (ou pressione Enter para manter o atual): ") #Solicita ao usuário que insira um novo nome para o prato ou pressione Enter para manter o nome atual
        novo_preco = input("Digite o novo preço do prato (ou pressione Enter para manter o atual): ") #Solicita ao usuário que insira um novo preço para o prato ou pressione Enter para manter o preço atual
        nova_descricao = input("Digite a nova descrição do prato (ou pressione Enter para manter a atual): ") #Solicita ao usuário que insira uma nova descrição para o prato ou pressione Enter para manter a descrição atual
       
        if novo_nome: #Se o usuário forneceu um novo nome, atualiza o nome do prato encontrado com o novo nome
            prato_encontrado["nome"] = novo_nome #Atualiza o nome do prato
        if novo_preco:                #Se o usuário forneceu um novo preço, tenta converter o valor para float e atualiza o preço do prato encontrado com o novo preço
            try:
                prato_encontrado["preco"] = float(novo_preco)   #Atualiza o preço do prato
            except ValueError:
                print("Preço inválido. Mantendo o preço atual.")  #Se o valor fornecido não puder ser convertido para float, exibe uma mensagem de erro e mantém o preço atual
        if nova_descricao:           
            prato_encontrado["descricao"] = nova_descricao   #Atualiza a descrição do prato encontrado com a nova descrição
        
        print("Prato atualizado com sucesso!")    
    else:
        print("Prato não encontrado.")

