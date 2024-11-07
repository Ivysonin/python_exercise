def contar_vogais(p) :
    # Vogais para verificar (TUPLA)
    vogais = ('a' , 'e' , 'i' , 'o' , 'u')

    # Contando quantas vogais tem
    contador = 0

    # Colocando minha palavra (p) em uma tupla(separando ela em letras)
    separador = tuple(p) 

    for i in separador :
        if i in vogais :
            contador += 1 # Adicionando +1 a cada vogal
    return contador

palavra = input ("Digite uma palavra: ").lower()

print (f"A palavra '{palavra}' possui {contar_vogais(palavra)} vogais")