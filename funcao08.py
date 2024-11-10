#                           EXERCICIO
# Crie uma função chamada 'soma_pares' que recebe uma lista de números inteiros.
# a função deve retorna a soma de todos os números pares da lista.
# Teste a função com uma lista de números, como [1,2,3,4,5,6], e veja se retorna o valor correto.

# Lista usada para adicionar números que o usuario escolher
usuario_lista = []

def soma_pares(n) :
    soma = 0
    for numero in n :
        if numero % 2 == 0 :
            soma += numero
        else:
            continue
    return soma

while True:
    numeros = int(input ("\n=== Digite Vários números inteiros (0 para sair): "))

    if numeros == 0 :
        print ("\n===== Você finalizou escolhas =====\n")
        break
    elif numeros != 0 :
        usuario_lista.append(numeros)
    else:
        print ("===== ERRO =====")

# Exibição final
print (f"=== Suas escolhas {usuario_lista}, Somando todos os números pares fica: {soma_pares(usuario_lista)} ")