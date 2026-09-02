#########################################
#CADASTRO ALEATORIO DE GARÇONS
##########################################

def sorteiame():
    import random
    numero_random = random.randint(1,30)
    return numero_random

for i in range(20):
    matricula = sorteiame()

    print("Garçom", i + 1)
    print("Nome: Garçom", i + 1)
    print("Matrícula:", matricula)
    print("Situação: Ativo")
    print()

#################################################
#CADASTRO MANUAL DE GARÇONS
################################################

def cadastrar_garcom():
    nome = input("Digite o nome do garçom: ")
    matricula = input("Digite a matrícula: ")
    situacao = input("Digite a situação profissional: ")

    return nome, matricula, situacao

nome, matricula, situacao = cadastrar_garcom()

print("\nDados cadastrados:")
print("Nome:", nome)
print("Matrícula:", matricula)
print("Situação:", situacao)

