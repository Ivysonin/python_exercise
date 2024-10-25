# Dada uma lista de palavras,
# conte quantos caracteres existem em cada palavra
# e armazene os resultados em uma nova lista.

palavras = ['python', 'exercicio', 'for', 'lista']

caracteres_palavra = []

for palavra in palavras:
    caracteres_palavra.append(len(palavra))

print (f"Nas palavras existem esse tanto de caracteres {caracteres_palavra}")