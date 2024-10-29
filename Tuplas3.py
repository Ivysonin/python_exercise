#                    EXERCICIO
# Crie uma tupla com as letras de uma palavra, por exemplo 
# palavra = ('p', 'y', 't', 'h', 'o', 'n').
# Conte quantas vogais existem na tupla e exiba o total.

palavra = ('p', 'y', 't', 'h', 'o', 'n')
vogais = ('a', 'e', 'i', 'o', 'u') # Criando uma tupla de vogais para fazer verificação

contador = 0
for letra in palavra : # estou pegando todas as 'letra' que estão na tupla 'palavra'
    if letra in vogais :
        contador += 1 # Se a 'letra' estiver dentro de 'vogais', eu adiciono + 1 a contador
    else:
        continue # Se não, só pular

print (f"Existem {contador} vogais na palavra !")