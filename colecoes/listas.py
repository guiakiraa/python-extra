# Criando a lista
lista = [12, 15.5, "texto"]

# Inserindo novos elementos
lista.insert(1, True) # Adiciona um elemento no índice informado
lista.append("Teste de inserção") # Adiciona um elemento no final da lista

# Mostrando a lista por inteiro
print(lista)

# Mostrando elemento pelo índice
print(lista[3])
print(lista[-1]) #Mostra o último elemento
print(lista[0:3]) #Mostra os elementos 0 ao 3

# Exibindo com loop
for valor in lista:
    print(valor)

# Removendo
lista.pop() # Remove o último elemento
print(lista)
lista.remove(12) # Remove pelo índice
print(lista)

# Tamanho da lista
print(len(lista))
