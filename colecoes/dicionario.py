#Dados
# Star Wars - Episódio IV - uma nova esperança, George Lucas, 1977, 775000000.00

# Criação do dicionário
dicionario = {
    "nome": "Star Wars - Episódio IV - uma nova esperança",
    "diretor": "George Lucas",
    "ano de lançamento": 1977,
    "bilheteria": 775000000.00
}

# Exibição do dicionário completo
print(dicionario)

# Exibição do valor de uma chave
print(dicionario["nome"])

# Inserção de uma nova chave e valor (gênero)
dicionario["gênero"] = "Space Opera"
print(dicionario)

# Método Keys
print(dicionario.keys()) # É uma estrutura ITERÁVEL -  pode ser usada em um FOR
for chave in dicionario.keys():
    print(chave)

# Método Values
print(dicionario.values())
for valor in dicionario.values():
    print(valor)

# Método items
print(dicionario.items())
for chave, valor in dicionario.items():
    print(f"{chave} -- {valor}")

# Método get
print(dicionario.get("público"))
print(dicionario.get("nome"))

# Método setdefault
dicionario.setdefault("publico", 1000)
print(dicionario)
dicionario.setdefault("publico", 9000) # Não altera, pois quando ele percebe que ja existe ele não realiza
print(dicionario)
