#               EXERCICIO
# Crie um programa para armazenar os contatos do zap em um
# dicionário de N pessoas. Cada pessoa pode ter o nome(chave) 
# e o valor(telefone). No final o programa deve exibir 
# na tela o nome e o tefefone dos contatos do zap !

contatos = {} # Dicionario vazio

print ("======== TELEFONE ========\n") # Organização
qnt_pessoas = int(input ("=== Digite quantos contatos quer adicionar: ")) # Quantidade de pessoas que o usuario quer adicionar

for i in range(qnt_pessoas) : # vai repetir a quantidade de vezes que o usuario escolheu em 'qnt_pessoas'
    nome = input ("Digite o nome: ")
    telefone = input ("Digite o telefone: ")
    contatos.update({nome : telefone})

print("\n======== Contatos Adicionados ========\n") # Organização

for chave,valor in contatos.items() : # Lista o nome junto do telefone de cada pessoa
    print (f"Nome: {chave} - Telefone: {valor}")