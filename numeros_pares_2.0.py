# Dada uma lista de números, crie uma nova lista contendo
# apenas os números pares da lista original.

numeros = [10, 21, 4, 45, 66, 93, 11]
pares = []

for num in numeros:
    if num % 2 == 0:
        pares.append(num)

print (f"Esses são os números pares {pares}")