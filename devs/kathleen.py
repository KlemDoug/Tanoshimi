lista_garcons = [
    {
        "matricula": "1001",
        "nome": "João da Silva",
        "situacao": "disponivel",
        "mesas_atribuidas": [1, 2, 3]
    },
    {
        "matricula": "1002",
        "nome": "Maria Oliveira",
        "situacao": "disponivel",
        "mesas_atribuidas": [4, 5]
    },
    {
        "matricula": "1003",
        "nome": "Carlos Santos",
        "situacao": "indisponivel",
        "mesas_atribuidas": []
    }
]


def consultar_garcom(lista_garcons):
    print("\n" + "=" * 40)
    print("CONSULTA DE GARÇOM - TANOSHIMI")
    print("=" * 40)

    if not lista_garcons:
        print("Nenhum garçom cadastrado no sistema até o momento.")
        return

    matricula_busca = input("Digite a matrícula do garçom: ").strip()

    if not matricula_busca:
        print("Matrícula inválida. O campo não pode ficar em branco.")
        return

    garcom_encontrado = None

    for garcom in lista_garcons:
        if str(garcom.get("matricula")) == matricula_busca:
            garcom_encontrado = garcom
            break

    if garcom_encontrado:
        print("\n--- DADOS DO PROFISSIONAL ---")
        print(f"Matrícula: {garcom_encontrado.get('matricula')}")
        print(f"Nome: {garcom_encontrado.get('nome')}")
        print(f"Situação: {garcom_encontrado.get('situacao', 'disponivel')}")

        mesas = garcom_encontrado.get("mesas_atribuidas", [])
        print(f"Mesas em Atendimento: {len(mesas)}")
        print("-" * 35)

    else:
        print(f"Garçom com a matrícula '{matricula_busca}' não foi encontrado.")



consultar_garcom(lista_garcons)