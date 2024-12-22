class Pessoa:
    def __init__(self, nome, idade): # Definindo as caracteristicas que todo objeto vindo da class vai ter
        self.nome = nome
        self.idade = idade

    def exibir_informacoes(self): 
        print(f"Nome: {self.nome}\nIdade: {self.idade}")

pessoa1 = Pessoa('Ivyson', '16')
pessoa1.exibir_informacoes()