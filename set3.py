# Set (Listas)
    # Funções em conjuntos set()
        # Evita itens duplicados
        # Não utiliza index


# Lista de conjunto set para teste
s1 = {1, 2, 3, 4, 5}


# Adicionando valor
s1.add(6)
# print(s1)


# Adicionando varios valores ao mesmo tempo
s1.update([7, 8, 9, 10])
# print(s1)


# Removendo itens do conjunto
    # se o item não estiver no conjunto, ele GERA um erro
s1.remove(10)
# print(s1)


# Discardando itens do conjunto
    # se o item não estiver no conjunto, ele NÃO gera um erro
s1.discard(9)
print(s1)