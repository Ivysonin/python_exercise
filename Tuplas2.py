#                     EXERCICIO
# Dada a tupla letras = ('a', 'b', 'a', 'c', 'b', 'a', 'd') 
# peça ao usuário para digitar uma letra e, em seguida 
# exiba quantas vezes essa letra aparece na tupla.

letras = ('a', 'b', 'a', 'c', 'b', 'a', 'd') # Defininddo uma tupla com string !

escolha = input ("=== Digite uma letra entre (a, b, c, d): ").lower() # Escolhendo qual letra eu quero contar, E transformando a mensagem em Minúscula.

contagem = letras.count(escolha) # Fazendo a contagem

print(f"A letra '{escolha}' aparece {contagem} vezes em tupla!") # Imprimindo resultado