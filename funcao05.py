# Extraindo número maior da lista
def maior_numero (n) :
    lista = max (n)
    return lista

# Lista vazia (será adicionado no futuro)
lista_numeros = []

# Organização
print ("===== Digite quantos números quiser. Para sair utilize '0' =====")

while True :
    numero = int(input ("\n=== Digite um número inteiro (0 para sair): "))

    if numero == 0 :
        break
    else:
        lista_numeros.append(numero)


print (f"\n===== O Maior número entre {lista_numeros}, é {maior_numero(lista_numeros)} =====")