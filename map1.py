# Map Function
    # Sintaxe: map(função, iterável)
    # Aplicar uma função a um Iterable, por item. (list, tuple, dict, etc)

def dobro(x: list) -> list:
    return x * 2


numeros = [1, 2, 3, 4, 5]

resultados = map(dobro, numeros)
print(list(resultados))

# Também pode ser usada com função lambda: map(lambda, iterável)
print(list(map(lambda x: x*2, numeros)))