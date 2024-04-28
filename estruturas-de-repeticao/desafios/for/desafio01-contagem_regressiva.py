# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de
# 10 até 0, com uma pausa de 1 segundo entre elas
from time import sleep

contador = 0
for contador in range(10, -1, -1):
    print(contador)
    sleep(1)
print("fogos estourando...")
