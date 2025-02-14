'''
🚀 Desafio: Primeira Letra das Palavras
Crie um programa em Python que utilize a função map para obter a primeira letra de cada palavra em uma lista.

💡 Instruções:
Crie uma lista com algumas palavras.
Use map para transformar essa lista em uma lista contendo apenas a primeira letra de cada palavra.
Exiba a lista original e a lista resultante.
'''

palavras = ['banana', 'morango', 'uva']


primeira_letra_palavra = list(map(lambda p: p[0] ,palavras))

print(f'Lista de palavras: {palavras}')
print(f'Primeiras letras: {primeira_letra_palavra}')