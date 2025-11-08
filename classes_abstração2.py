from abc import ABC, abstractmethod


# Abstração
class Animal(ABC):
    @abstractmethod
    def fazer_som(self):
        pass

# Concretização da abstração
class Cachorro(Animal):
    def fazer_som(self):
        return "Au au..."

class Gato(Animal):
    def fazer_som(self):
        return "Miau miau..."

cachorro = Cachorro()
print(cachorro.fazer_som()) # Saída: Au au...

gato = Gato()
print(gato.fazer_som()) # Saída: Miau miau...