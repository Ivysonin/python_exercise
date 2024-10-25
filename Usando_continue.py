# Escreva um programa que percorra os números de 1 a 20, e para cada número:
# Se o número for divisível por 3, pule (use continue).
# Caso contrário, imprima o número.

numeros = range(0,21) # O número vai ser entre 1 a 20

for numero in numeros: # crio uma variavel que está dentro de 'numeros'
    if numero % 3 == 0: # Se numero for dividido por 3, ele pula 
        continue
    else:
        print (numero) # ele imprimi(mostra) o 'numero'