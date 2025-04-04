# Classe mãe: Todos os animais podem herdar esses atributos
class Animal:
    def __init__(self, nome):
        self.nome = nome

    def comer(self):
        print(f'{self.nome} está comendo')

    def dormir(self):
        print(f'{self.nome} está dormindo')


# Classes filhas
class Cachorro(Animal):
    def latir(self):
        print('au au')
    
    def buscar_bola(self):
        print(f'{self.nome} está buscando a bola')


class Gato(Animal):
    def miar(self):
        print('miau miau')

    def arranhar(self):
        print(f'{self.nome} está arranhando o sofá')


class Passaro(Animal):
    def cantar(self):
        print(f'{self.nome} está cantando')


class Cavalo(Animal):
    def galopar(self):
        print(f'{self.nome} está galopando')


print('') # Pulando linha para melhor visualização 

# Testando os atributos

cachorrinho = Cachorro('cachorrinho')
cachorrinho.latir()
cachorrinho.buscar_bola()
cachorrinho.comer()
cachorrinho.dormir()

print('') # Pulando linha para melhor visualização 

gatinho = Gato('gatinho')
gatinho.miar()
gatinho.arranhar()
gatinho.comer()
gatinho.dormir()

print('') # Pulando linha para melhor visualização 

passarinho = Passaro('passarinho')
passarinho.cantar()

print('') # Pulando linha para melhor visualização 

cavalinho = Cavalo('cavalinho')
cavalinho.galopar()
cavalinho.comer()
cavalinho.dormir()