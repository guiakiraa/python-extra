# Crie um progama que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram
# a maioridade e quantas ja são de maiores

contador = 0
for i in range(0, 7, 1):
    anoNascimento = int(input("Informe sua data de nascimento: "))
    if 2024 - anoNascimento >= 18:
        contador +=1
print(f"{contador} pessoas já são de maiores e {7-contador} ainda não atingiram a maioridade! ")