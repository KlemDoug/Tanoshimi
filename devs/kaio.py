mesas_sistema = [
    {
        "numero_mesa": 1,
        "capacidade": 2,
        "status": "indisponivel"
    },
    {
        "numero_mesa": 2,
        "capacidade": 2,
        "status": "disponivel"
    },
    {
        "numero_mesa": 3,
        "capacidade": 2,
        "status": "disponivel"
    },
    {
        "numero_mesa": 4,
        "capacidade": 4,
        "status": "disponivel"
    },
    {
        "numero_mesa": 5,
        "capacidade": 4,
        "status": "disponivel"
    },
    {
        "numero_mesa": 6,
        "capacidade": 4,
        "status": "disponivel"
    },
    {
        "numero_mesa": 7,
        "capacidade": 8,
        "status": "indisponivel"
    },
    {
        "numero_mesa": 8,
        "capacidade": 8,
        "status": "indisponivel"
    },
    {
        "numero_mesa": 9,
        "capacidade": 8,
        "status": "indisponivel"
    },
]

# não apagar para garantir a preservação do historico
def imprimir_mesas_disponiveis(mesas_2_p, mesas_4_p, mesas_8_p):
    if(len(mesas_2_p) > 0):
        print("As mesas dispóniveis para duas pessoas são as mesas número: ", mesas_2_p)
    else:
        print("As mesas de dois lugares estão indispóniveis")

    if(len(mesas_4_p) > 0):
        print("As mesas dispóniveis para quatro pessoas são as mesas número: ", mesas_4_p)
    else:
        print("As mesas de quatro lugares estão indispóniveis")

    if(len(mesas_8_p) > 0):
        print("As mesas dispóniveis para oito pessoas são as mesas número: ", mesas_8_p)
    else:
        print("As mesas de oito lugares estão indispóniveis no momento.")
    
    if(len(mesas_2_p) == 0 and len(mesas_4_p) == 0 and len(mesas_8_p) == 0):
        print("Nenhuma mesa dispónivel no sistema. :( ")


def listar_mesas(mesas):
    mesa_history = mesas

    if(len(mesas) <= 0 or type(mesas) != list):
      print("Error! O valor passado é inválido!");
      return;
    
    mesas_disponiveis = [];

    # Separação em matrizes
    mesas_2_pessoas = []
    mesas_4_pessoas = []
    mesas_8_pessoas = []
    
    for i in mesas:
      if(i['status'] == "disponivel"):
         mesas_disponiveis.append(i);
      
      if(i['status'] == "disponivel" and i['capacidade'] == 2):
        mesas_2_pessoas.append(i["numero_mesa"])

      if(i['status'] == "disponivel" and i['capacidade'] == 4):
        mesas_4_pessoas.append(i["numero_mesa"])

      if(i['status'] == "disponivel" and i['capacidade'] == 8):
        mesas_8_pessoas.append(i["numero_mesa"])
    
    ## Interação com o usuario
    print("Bem-Vindo! Temos:", len(mesas_disponiveis),"mesas disponiveis no sistema.")
 
    while True:
     try:
         quantidade_lugares = int(input("Você gostaria de quantos lugares? (Digite 0 para listar mesas dispóniveis): "))
         if(quantidade_lugares == 0):
             imprimir_mesas_disponiveis
             break
         
     except ValueError:
         print("Erro! O valor digitado tem que ser um número")
 
    imprimir_mesas_disponiveis(mesas_2_pessoas, mesas_4_pessoas, mesas_8_pessoas)
    return mesa_history


listar_mesas(mesas_sistema)