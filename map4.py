'''
🚀 Desafio: Comprimento das palavras
Crie um programa em Python que utilize a função map para calcular o comprimento de cada palavra em uma lista.

💡 Instruções:
Crie uma lista com algumas palavras.
Use map para transformar essa lista em uma lista com os tamanhos das palavras.
Exiba a lista original e a lista com os comprimentos.
'''


lista_palavras = ['python', 'ivyson', 'elisete', 'brasil']

resultado = list(map(len, lista_palavras))

print(f'Lista de palavras: {lista_palavras}')
print(f'Tamanhos das palavras: {resultado}')