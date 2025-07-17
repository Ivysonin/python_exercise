# Desafio:
# Você tem esta lista de tuplas, onde cada tupla representa um produto e seu preço:
# produtos = [('Celular', 1200), ('Notebook', 3500), ('Fone', 200), ('Monitor', 800)]
# Ordene a lista de forma crescente com base no valor dos produtos. 
# Nada de mexer diretamente nos índices, hein — use o key com lambda


produtos = [('Celular', 1200), ('Notebook', 3500), ('Fone', 200), ('Monitor', 800)]

produtos = sorted(produtos, key=lambda x: x[1])

print(produtos)