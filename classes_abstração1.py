from abc import ABC, abstractmethod


# Abstração
class Veiculo(ABC):
    @abstractmethod
    def mover(self):
        pass

# Concretização da abstração
class Carro(Veiculo):
    def __init__(self, marca: str, cor: str):
        self.marca = marca
        self.cor = cor

    def mover(self):
        return 'Acelerando o carro...'


carro = Carro('BMW', 'Azul')
print(carro.mover()) # Saída: Acelerando o carro...