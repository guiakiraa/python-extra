# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros
# termos dessa progressão.

numero = int(input("Informe o 1° termo da PA: "))
razao = int(input("Informe a razão da PA: "))
print(f"Os dez primeiros termos da PA de {numero} com razão de {razao} são: ")
for i in range(0, 10, 1):
    numero += razao
    print(numero)