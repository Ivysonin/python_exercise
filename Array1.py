# Arrays (Matriz)
    # Similar a listas
    # Melhor performance
    # Usada para mais de 1k de itens em listas

from array import array

letras = array('u', ['a', 'b', 'c', 'd'])
numeros_i = array('i', [1, 3, 5, 6, 23, 7])
numeros_f = array('f', [1.2, 3.5, 7.4])

print()
print(letras)
print(numeros_i)
print(numeros_f)