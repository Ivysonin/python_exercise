# Crie um objeto da classe Retangulo, defina os valores e mostre a área e o perímetro.

class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
    
    def calcular_area(self):
        return self.largura * self.altura
    
    def calcular_perimetro(self):
        P = 2 * (self.largura + self.altura) # fórmula para calcular o perimetro (  P=2(b+h)  )
        return P
    
retangulo = Retangulo(7, 3)

print(f"Aréa: {retangulo.calcular_area()}")
print(f"Perimetro: {retangulo.calcular_perimetro()}")