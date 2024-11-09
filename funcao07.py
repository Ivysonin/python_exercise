#               EXECICIO
# Contar quantas vogais tem em uma frase
vogais = ["a", "e", "i", "o", "u",]

def contar_vogais (n) :
    # para contar quantas vogais tem
    contador = 0

    for letra in n :
        if letra in vogais :
            contador += 1
        else:
            continue
    return contador

# Escolha usuario
frase = input ("=== Digite uma frase: ").lower()

# Exibição final
print (f"\n=== A frase '{frase}' tem {contar_vogais(frase)} Vogais ===")