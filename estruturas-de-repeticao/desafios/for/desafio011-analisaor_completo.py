# Crie um programa que leia nome, idade e sexo de 4 pessoas. No final do programa, mostra:
# A média de idade do grupo; Qual é o nome do homem mais velho; Quantas mulheres têm menos de 20 anos.

somaIdades = 0
maisVelho = 0
nomeMaisVelho = ""
menosVinteAnos = 0
contadorHomem = 0
for i in range(0, 4, 1):
    nome = str(input("Nome: "))
    idade = int(input("Idade: "))
    sexo = str(input("Sexo(M/F): ")).upper()
    somaIdades += idade
    if sexo == "M":
        contadorHomem += 1
        if idade > maisVelho:
            nomeMaisVelho = nome
    if sexo == "F":
        if idade < 20:
            menosVinteAnos +=1
mediaIdades = somaIdades / 4

print(f"A média das idades é {mediaIdades}.")

if contadorHomem > 1:
    print(f"O homem mais velho se chama {nomeMaisVelho}.")
else:
    print("Não foi informado nenhum homem")

if menosVinteAnos > 1:
    print(f"{menosVinteAnos} mulheres tem menos de 20 anos.")
elif menosVinteAnos == 1:
    print(f"{menosVinteAnos} mulher tem menos de 20 anos")
else:
    print("Nenhuma mulher tem mais de 20 anos")