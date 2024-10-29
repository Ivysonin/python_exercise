#                   EXERCICIO
# Dada a tupla numeros = (5, 3, 5, 2, 5, 3, 1, 5, 2) 
# crie um código que conte quantas vezes o número 5 aparece na tupla.

numeros = (5, 3, 5, 2, 5, 3, 1, 5, 2) # Tupla imutável: não pode ser alterada !
elemento = 5

contagem = numeros.count(elemento) # Estou contando quantas vezes aparece o 'elemento' em 'numeros'

print (f"O número {elemento} aparece {contagem} vezes na Tupla!") # imprimindo mensagem organizada