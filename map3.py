'''
🚀 Desafio: Dobrar os números ímpares
Crie um programa em Python que utilize a função map para dobrar apenas os números ímpares de uma lista.

💡 Instruções:
Crie uma lista com números inteiros.
Use map para dobrar os números ímpares e manter os pares inalterados.
Exiba a lista original e a lista modificada.
'''

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

resultado = list(map(lambda n: n*2 if n % 2 != 0 else n, numeros))

print(f'Lista original: {numeros}')
print(f'Lista modificada: {resultado}')