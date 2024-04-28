# Crie um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

maior = 0
menor = 1000000
for i in range(0, 5, 1):
    peso = int(input("Informe seu peso: "))
    if peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso
print(f"""
O maior peso foi: {maior};
O menor peso foi: {menor}.
""")