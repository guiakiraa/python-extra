# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderandos os espaços.

frase = input("Digite uma frase: ").strip().upper()
palavras = frase.split()
junto = "".join(palavras)
inverso = ""
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print(f"{junto} {inverso}")
if inverso == junto:
    print(f"{frase} é um palíndromo")
else :
    print(f"{frase} não é um palíndromo")