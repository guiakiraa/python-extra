# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

numero = int(input("Informe o número que deseja verificar se é primo: "))
restoDivisao = 0
for i in range(numero -1 , 1, -1):
    if numero % i == 0:
        restoDivisao = 1
if restoDivisao == 1:
    print(f"{numero} não é um número primo!")
else:
    print(f"{numero} é um número primo!")