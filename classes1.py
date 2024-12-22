class Aluno:
    def __init__(self,nome):
        self.nome = nome
        self.notas = []
        self.media = 0

    def adicionar_nota(self,nota):
        self.notas.append(nota)

    def calcular_media(self):
        # Variavel 'nota = 0' sendo usada para somar os valores que estão na list
        nota = 0
        for i in self.notas:
            nota += i
            self.media = nota / 2 # dividindo apenas por 2, pq eu só estou atribuindo 2 notas.
        return self.media

    def exibir_dados(self):
        print(f"Nome: {self.nome}\nMédia: {self.media}")

# Criando alunos
aluno1 = Aluno('Iyvson')

# Adicinando notas
aluno1.adicionar_nota(5)
aluno1.adicionar_nota(10)

# calculando media
aluno1.calcular_media()

# Exibindo
aluno1.exibir_dados()