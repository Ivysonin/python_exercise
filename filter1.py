'''
Estrutura: filter(func, iterable)

func: Uma função que retorna True ou False para cada elemento
iterable: A sequência (lista, tupla, etc.) que será filtrada

Essa função é super útil para simplificar operações de filtragem de dados, especialmente quando combinada com expressões lambda.
'''

lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

par = filter(lambda num: num % 2 == 0, lista_numeros)

# Exibindo
print(list(par))