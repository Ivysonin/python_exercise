# Set (Listas)
    # Funções de set usando str()


# Listas de conjuntos set para testes
set1 = {'a', 'b', 'c'}
set2 = {'a', 'd', 'e'}
set3 = {'c', 'd', 'f'}


# Adiciona na nova variavel set4
    # a união do set1 com set2, sem exibir os valores duplicados
set4 = set1.union(set2)
# print(set4)


# Mostra a diferença entre os conjuntos
    # Nesse exemplo é: {'a', 'b'}
    # porque eu pedir a diferença do set1 para o set3
set5 = set1.difference(set3)
# print(set5)


# Mostra o que eu tenho tanto em um como no outro
    # Nesse exemplo é: {'a'}
set6 = set1.intersection(set2)
# print(set6)


# Ele retira aquele que está tando em um conjunto como no outro
    # Nesse exemplo ele mostra: {'f', 'd', 'b', 'a'}
    # E esconde: {'c'}
set7 = set1.symmetric_difference(set3)
print(set7)