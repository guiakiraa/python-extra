opcao = 0
while opcao != 3:
    print("""
    ----------MENU----------
    1 - Receber um elogio: 
    2 - Calcular fatorial: 
    3 - Sair
    """)
    opcao = int(input("Por favor, escolha uma opção: "))
    match opcao:
        case 1:
            print("Você é muito inteligente! ")
        case 2:
            numero = int(input("Por favor, informe o número que deseja o fatorial: "))
            fatorial = numero
            for valor in range(1, numero, 1):
                fatorial = fatorial * valor
            print(f"O fatorial de {numero} é {fatorial}")
        case 3:
            print("Saindo do sistema ...")
        case _:
            print("Escolha uma opção válida! ")