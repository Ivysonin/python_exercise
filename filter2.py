lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

impar = filter(lambda num: num % 2 != 0, lista_numeros)

print(list(impar))