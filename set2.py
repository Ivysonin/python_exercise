# Exercicio usando conjuntos set()
    # Saber quantos amigos tem em comum entre 2 amigos
    # Adicionar os amigos a uma lista, transforma a lista em set e compara os amigos em comum
    # Exibindo no final os amigos os amigos


# Lista para armazenar os amigos
lista_de_amigos1 = []
lista_de_amigos2 = []

# Pegando o nome de 2 amigos
nome_amigos = input('\n===== Siga as instruções a seguir =====\n\n'
               '- Escreva o nome de vocês(apenas 2 nomes)\n'
               '- Siga esse formato: Nome,Nome\n Digite o nome de vocês: ')

# Separando os nomes pela vírgula e transformando em list
nome_amigos = list(nome_amigos.split(','))

print() # Organização

# Primeiro amigo
for i in range(3):
    amigos = input(f'Para o amigo "{nome_amigos[0]}", escreva um amigo: ')
    lista_de_amigos1.append(amigos)

print() # Organização

# Segundo amigo
for i in range(3):
    amigos = input(f'Para o amigo "{nome_amigos[1]}", escreva um amigo: ')
    lista_de_amigos2.append(amigos)

# Exibição final
print('\nOs amigos que vocês tem em comum são:\n'
      f'{(set(lista_de_amigos1)) & (set(lista_de_amigos2))}')