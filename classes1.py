class Notas():
    def __init__(self, nome):
        self.nome = nome
        self.at1 = 0 
        self.at2 = 0

    def atividade(self, at):
        self.at1 = at

    def prova(self, at2):
        self.at2 = at2

    def media(self):
        if (self.at1 + self.at2) / 2 >= 8:
            print(self.nome, "Nota: A")
        elif (self.at1 + self.at2) / 2 <= 6 and (self.at1 + self.at2) / 2 > 0 :
            print (self.nome, "Nota: B")
    
aluno_1 = Notas('Ivyson')
aluno_1.atividade(10)
aluno_1.prova(2)
aluno_1.media()

aluno_2 = Notas('Ana')
aluno_2.atividade(10)
aluno_2.prova(10)
aluno_2.media()