# Não suportam repetição de valores

# Criando um set vazio
conjunto = set()

# Criando um set a partir de uma lista
lista = ["André", "Davi", "Cebolinha", "André"]
print(lista)
conjunto2 = set(lista)
print(conjunto2) # Não repete o André

# Criando um ser com valores
conjunto3 = {"Cebolinha", "Magali", "Mônica", "Cebolinha"}
print(conjunto3) # Não repete o Cebolinha

# Adicionando um elemento(add)
conjunto3.add("Franjinha")
print(conjunto3)

# Removendo elementos que estão em outro set (difference_update)
conjunto1 = {"Mega Drive", "Super Nintendo", "Playstation"}
conjunto2 = {"Playstation", "Nintendo 64", "Sega Saturn", "Dreamcast"}
print(f"O primeiro set contém {conjunto1}")
print(f"O segundo set contém {conjunto2}")
conjunto1.difference_update(conjunto2)
print(conjunto1)

# Remover um elemento específico do set (remove)
conjunto1 = {"Mega Drive", "Super Nintendo", "Playstation"}
print(conjunto1)
conjunto1.remove("Mega Drive")
print(conjunto1)
#conjunto1.remove("Mega Drive")

# Remover um elemento específico do set (remove)
conjunto1.discard("Super Nintendo")
print(conjunto1)
conjunto1.discard("Super Nintendo")
print(conjunto1)
