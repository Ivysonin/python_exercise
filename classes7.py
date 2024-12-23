class Livro:
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano

    def descricao(self):
        return print(f"Título: {self.titulo}\nAutor: {self.autor}\nAno: {self.autor}")
    
# Criando livros
livro1 = Livro('Naruto', 'Masashi Kishimoto', '1974')

# Exibindo as informações
livro1.descricao()