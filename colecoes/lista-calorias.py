calorias = []
resposta = ""

while resposta.upper() != "NÃO":
    caloria = int(input("Quantas calorias você consumiu nessa refeição: "))
    calorias.append(caloria)
    resposta = input("Você deseja informar as calorias de mais uma refeição: ")

total = 0
contador = 0
for caloria in calorias:
    contador = contador + 1
    print(f"Na {contador}° refeição você consumiu {caloria} calorias")
    total += caloria
mediaCalorias = total / len(calorias)
print(f"A média de calorias consumidas foi de {mediaCalorias:.2f} calorias")