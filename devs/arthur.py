#Projeto dp modulo 1

#Registrar pagamento
#Registrar valor, forma de pagamento, data e situação

# numero_da_conta = "a definir"
# valor = "a definir"

#numero_da_conta = float(input("Informe o numero da conta: "))

def cadastrar_pagamento():
    numero_da_conta = float(input("Informe o numero da conta:"))
    valor = float(input("Informe o valor a ser pago: "))
    print ("Forma de pagamento: ")
    print ("1-Pix")
    print ("2-Cartão")
    print ("3-Dinheiro")

    opcao_de_pagamento = float(input("Escolha a forma de pagameto: "))

    match opcao_de_pagamento:
        case 1:
            forma_de_pagamento = "Pix"
        case 2:
            forma_de_pagamento = "Cartão"
        case 3:
            forma_de_pagamento = "Dinheiro"
        case _:
            print("Opção invalida")
    
    situacao = input("Pagamento realzado com sucesso (sim/nao) ? ")
    if situacao == "sim":
        print("Numero da conta",numero_da_conta,"pagamento realizado com sucesso.")
    else:
        print("Tente de novamente")

    Registro_de_pagamento = {
    'numero_da_conta':'Pago',
    'forma_pagamento' : 'forma_de_pagamento'
    }




# consulta_pagamento = ("montar")