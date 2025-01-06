# Crie uma função que aceite um número como argumento e retorne True se o número for par 
# e False se for ímpar. 
# Teste a função com diferentes valores.

def par_impar(numero):
    if numero % 2 == 0:
        return True
    else:
        return False


numero = 15

print(par_impar(numero))