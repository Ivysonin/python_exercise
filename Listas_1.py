# Crie uma lista com cinco números inteiros (o usuario escolhe). 
# Em seguida, remova o primeiro e o último número. Exiba a lista resultante.

lista_numeros = []

print ("===== Adicionando Números a uma lista =====\n")

# Adicionando Números a lista

num1 = int(input ("Digite um número para adicionar a lista: "))
lista_numeros.append(num1) # Adicionando o valor 'num1' a minha lista 'lista_numeros'

num2 = int(input ("Digite um número para adicionar a lista: "))
lista_numeros.append(num2) # Adicionando o valor 'num2' a minha lista 'lista_numeros'

num3 = int(input ("Digite um número para adicionar a lista: "))
lista_numeros.append(num3) # Adicionando o valor 'num3' a minha lista 'lista_numeros'

num4 = int(input ("Digite um número para adicionar a lista: "))
lista_numeros.append(num4) # Adicionando o valor 'num4' a minha lista 'lista_numeros'

num5 = int(input ("Digite um número para adicionar a lista: "))
lista_numeros.append(num5) # Adicionando o valor 'num5' a minha lista 'lista_numeros'

print (f"Aqui está sua lista {lista_numeros}\n")

print ("===== Removendo o Primeiro e último número =====")
# Removendo os números selecionados
lista_numeros.remove(num1)
lista_numeros.remove (num5)

print (f"===== Sua lista sem o primeiro e o último número {lista_numeros}")