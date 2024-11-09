# Extraindo número maior da lista
def maior_numero (n) :
    lista = max(n)
    return lista

# Lista vazia (será adicionado no futuro)
lista_numeros = []

# Organização
print ("===== Digite quantos números quiser. Para sair utilize '0' =====")

while True :
    numero = int(input ("\n=== Digite um número inteiro (0 para sair): "))

    if numero != 0 :
        lista_numeros.append(numero)
    elif numero == 0 :
        print ("\n=== Você encerrou o programa ===")
        break
    else:
        print ("\n=== ERRO ===\n")

print (f"\n===== Você digitou {lista_numeros} o maior número entre os que você digitou é '{maior_numero(lista_numeros)}' =====")