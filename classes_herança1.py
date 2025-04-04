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


class Gato(Animal):
    def miar(self):
        print('miau miau')


class Passaro(Animal):
    def cantar(self):
        print(f'{self.nome} está cantando')



# Testando os atributos

cachorrinho = Cachorro('cachorrinho')
cachorrinho.latir()
cachorrinho.comer()
cachorrinho.dormir()

print('') # Pulando linha para melhor visualização 

gatinho = Gato('gatinho')
gatinho.miar()
gatinho.comer()
gatinho.dormir()

print('') # Pulando linha para melhor visualização 

passarinho = Passaro('passarinho')
passarinho.cantar()