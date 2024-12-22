class Contador:
    def __init__(self):
        self.valor_inicializado = 0

    def incrementar(self):
        self.valor_inicializado += 1
        return self.valor_inicializado
    
    def decrementar(self):
        self.valor_inicializado -= 1
        return self.valor_inicializado
    
    def zerar(self):
        self.valor_inicializado = 0
        return self.valor_inicializado

    def mostrar_valor(self):
        return print(f"Valor: {self.valor_inicializado}")

numero = Contador()

# Atribuindo 1
print(numero.incrementar())
print(numero.incrementar())
print(numero.incrementar())
numero.mostrar_valor() # mostrando valor

# Diminuindo 1
print(numero.decrementar())
numero.mostrar_valor() # mostrando valor

# zerar
numero.zerar()
numero.mostrar_valor() # mostrando valor