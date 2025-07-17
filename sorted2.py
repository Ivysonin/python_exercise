# Desafio:
# Você tem uma lista com palavras: ['carro', 'bicicleta', 'ônibus', 'avião', 'moto'].
# Ordene essa lista com base no tamanho das palavras, ou seja, da mais curta pra mais longa.
# Dica: vai precisar passar uma função para o parâmetro key


lista_palavras = ['carro', 'bicicleta', 'ônibus', 'avião', 'moto']

lista_palavras = sorted(lista_palavras, key=lambda x: len(x))

print(lista_palavras)