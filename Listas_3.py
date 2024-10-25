# EXERCICIO:
# Construa uma lista de cinco frutas (usuario escolhe). 
# Ordene a lista em ordem alfabética e depois exiba apenas a terceira fruta.
# ###########################################################################
# Dei uma melhorada no exercicio

lista_frutas = []

print ("===== Lista de Frutas =====\n")

# Adicionando frutas a lista

fruta1 = input ("escolha uma fruta: ")
lista_frutas.append(fruta1)

fruta2 = input ("escolha uma fruta: ")
lista_frutas.append(fruta2)

fruta3 = input ("escolha uma fruta: ")
lista_frutas.append(fruta3)

fruta4 = input ("escolha uma fruta: ")
lista_frutas.append(fruta4)

fruta5 = input ("escolha uma fruta: ")
lista_frutas.append(fruta5)

print ("\n===== Escolha sua fruta favorita que esteja na sua lista =====")
print ("=== Lista: ")

for i in lista_frutas: # Listando a 'lista_frutas'
    print (f"- {i}") # Listando para melhor visualização

# Estrutura que escolhe sua fruta favorita

fruta_favorita = input ("Escolha a fruta (escreva exatamente como está acima): ")

if fruta_favorita == fruta1 :
    print (f"=== Sua fruta favorita é: {fruta1}")
elif fruta_favorita == fruta2 :
    print (f"=== Sua fruta favorita é: {fruta2}")
elif fruta_favorita == fruta3 :
    print (f"=== Sua fruta favorita é: {fruta3}")
elif fruta_favorita == fruta4 :
    print (f"=== Sua fruta favorita é: {fruta4}")
elif fruta_favorita == fruta5 :
    print (f"=== Sua fruta favorita é: {fruta5}")
else:
    print ("Não seguio instruções !!")