# Set (Listas)
    # Similiar a listas
    # Evita itens duplicados
    # Não utiliza index


list1 = [10, 20, 30, 40]
list2 = [10, 20, 50, 60]

num1 = set(list1)
num2 = set(list2)

# Une 2 listas sem os valores repitidos
print(num1 | num2) # | se chama (union)


# Mostra a diferença entre as listas, nesse caso 40 and 30 porque é a diferença entre elas
    # A ordem das variaveis interfe no resultado
print(num1 - num2) # - se chama (difference)


# Mostra os valores, removendo os repetidos das 2 listas, no caso 10 and 20
print(num1 ^ num2) # ^ se chama (Symmetric difference)


# Mostra oque é duplicado em uma lista e em outra. No caso 10 and 20
print(num1 & num2) # & se chama (And)


# Não é possível acessar o index da lista, porque não existe index em conjuntos set
print(num1[0])