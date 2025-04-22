'''
🔍 Exercício: Filtrar Palavras com Mais de 5 Letras

Crie uma função chamada palavras_grandes que receba uma lista de palavras (strings) e retorne apenas as palavras que têm mais de 5 letras, usando a função filter.

Exemplo:
lista = ["casa", "elefante", "sol", "maravilhoso", "gato"]
Saída esperada: ["elefante", "maravilhoso"]
'''

lista = ["casa", "elefante", "sol", "maravilhoso", "gato"]

palavra_com_Cinco_letras = filter(lambda palavra: len(palavra) > 5, lista)

print(list(palavra_com_Cinco_letras))