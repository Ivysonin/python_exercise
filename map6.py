'''
🚀 Desafio: Última Letra das Palavras
Crie um programa em Python que utilize a função map para obter a última letra de cada palavra em uma lista.

💡 Instruções:
Crie uma lista com algumas palavras.
Use map para transformar essa lista em uma lista contendo apenas a última letra de cada palavra.
Exiba a lista original e a lista resultante.
'''

lista_palavras = ["banana", "abacaxi", "uva", "morango", "kiwi"]

ultima_letra_palavra = list(map(lambda p: p[-1], lista_palavras))

print(f'Lista de palavras: {lista_palavras}')
print(f'Últimas letras: {ultima_letra_palavra}')