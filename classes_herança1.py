# Classe mãe: Todos os animais podem comer e dormir
class Animal:
    def __init__(self, nome):
        self.nome = nome

    def comer(self):
        print(f'{self.nome} está comendo')

    def dormir(self):
        print(f'{self.nome} está dormindo')


# Classe filha: Apenas o cachorro pode latir
class Cachorro(Animal):
    def latir(self):
        print('au au')
# Classe filha: Apenas o gato pode miar
class Gato(Animal):
    def miar(self):
        print('miau miau')


cachorrinho = Cachorro('bob')
cachorrinho.latir()
cachorrinho.comer()
cachorrinho.dormir()

print('')

gatinho = Gato('lilo')
gatinho.miar()
gatinho.comer()
gatinho.dormir()