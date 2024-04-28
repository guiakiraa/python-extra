opcao = 0
ficha = {}
while opcao != 4:
    print("""
    FICHA CADASTRAL
    1 - Incluir informações na ficha
    2 - Recuperar informações da ficha
    3 - Exibir a ficha completa
    4 - Sair
    """)
    opcao = int(input("Informe a opção desejada: "))

    match opcao:
        case 1:
            # inserir dados na ficha
            chave = input("Informe o campo que deseja cadastrar na ficha: ")
            valor = input("Informe o dado que deseja cadastrar neste campo: ")
            #ficha[chave] = valor
            ficha.update({chave: valor})

        case 2:
            # recuperar dados da ficha
            print(f"Os campos disponíveis na ficha são {ficha.keys()}")
            chave = input("Informe qual campo deseja exibir: ")
            if chave in ficha.keys():
                print(f"O campo {chave} contém o dado {ficha.get(chave)}")
            else:
                print("Você digitou um campo inexistente.")

        case 3:
            # exibir ficha completa
            print("FICHA CADASTRAL")
            for campo, dado in ficha.items():
                print(f"{campo.upper()}: {dado}")
        case 4:
            print("Saindo do sistema de ficha cadastral")
            break
        case _:
            print("Opção inválida! Escolha uma opção válida.")