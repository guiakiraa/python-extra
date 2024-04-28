# Faça uma tabuada usando o for

numero = int(input("Número: "))
soma = 0
for contador in range(1, 11, 1):
    soma = numero * contador
    print(f"{numero} x {contador} = {soma}")