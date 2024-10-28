# Fazer sistema de adicionar jogadores
# 1 - Fazer uma lista para jogadores
# 2 - Fazer uma lista de habilidade
# 3 - Fazer uma lista de preferência de marca como nike ou adidas

# Listas
jogadores_nomes = []
jogadores_habilidades = []
jogadores_marcas = []

print ("====== Adicione Jogadores ======\n") # Organização

qnt_jogadores = int(input ("=== Digite quantos jogadores quer adicionar: "))

for i in range(qnt_jogadores) : 
    nome = input ("Digite o nome: ")
    jogadores_nomes.append(nome)

    habilidade = input ("Digite UMA habilidade do jogador: ")
    jogadores_habilidades.append(habilidade)

    marca = input ("Digite a Marca do jogador: ")
    jogadores_marcas.append(marca)

print ("\n====== Jogadores Adicionados:\n") # Organização

for i in range(qnt_jogadores) :
    print (f"Nome: {jogadores_nomes [i]}") # O 'i' serve para pegar tudo que está dentro da lista
    print (f"Habilidade: {jogadores_habilidades [i]}")
    print (f"Marca: {jogadores_marcas [i]}")
    print ("") # Organização