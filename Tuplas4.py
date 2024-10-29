#                                     EXERCICIO
# Dada a tupla itens = (1, 'a', 2, 'b', 'a', 3, 'a', 1) 
# escreva um código para contar quantas vezes o valor 'a' e o valor 1 aparecem na tupla.

# Tupla:
itens = (1, 'a', 2 , 'b', 'a', 3, 'a', 1)

# Elementos:
elemento_int = 1
elemento_str = 'a'

# Fazendo contagem dos elementos:
contagem_int = itens.count(elemento_int) # 'int' porque é número
contagem_str = itens.count(elemento_str) # 'str' porque é letra, palavra, etc...

print (f"O elemento '{elemento_str}' aparece {contagem_str} vezes em tupla.") # Imprimindo o 'str' para melhor visualização
print (f"O elemento '{elemento_int}' aparece {contagem_int} vezes em tupla.") # Imprimindo o 'int' para melhor visualização