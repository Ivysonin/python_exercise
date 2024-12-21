# Classe para fazer os registros dos pokémons como: nome, tipo e fraqueza
class Pokedex() :
    def __init__(self, nome):
        self.nome = nome
        self.tipo = str
        self.fraqueza = str

    def nome_pokemon(self):
        return self.nome

    def definir_tipo(self): 
        self.tipo = input(f"Digite o elemento do pokémon {self.nome}: ")
        return self.tipo
    
    def definir_fraqueza(self):
        self.fraqueza = input(f"Digite a fraqueza do pokémon {self.nome}: ")
        return self.fraqueza

# Adicionando o pokémon
pokemon = Pokedex(input("Digite o nome do pokémon: "))

# Criando uma list com 3 dict dentro, para salvar as alteração do pokémon
informacoes_pokemon = [
    {'Nome' : pokemon.nome_pokemon()},
    {'Tipo' : pokemon.definir_tipo()},
    {'Fraqueza' : pokemon.definir_fraqueza()}
]

# Exibindo
for indice in informacoes_pokemon:
    for valores in indice:
        print(f"{valores}: {indice[valores]}") # O 'indice' ele pega o conjunto de 'chave : valor' dentro do dict que está dentro da list, para não exibir a mesma coisa uso o 'valores' para pega apenas as chaves e depois uso o 'indice[valores]' para pegar apenas os valores.