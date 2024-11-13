from random import randint

# lista com herois
heroi = ["Batman" , "Superman"]

# Listas para adicionar os valores
batman = []
superman = []

def competicao(heroi) :
    tentativas_batman = 3
    soma_batman = 0
    tentativas_superman = 3
    soma_superman = 0

    print (f"=== {heroi[0]} dá uma volta na cidade e:\n")
    for i in range(tentativas_batman) :
        numero = randint(50, 100)
        print(f"Na sua {i+1}º tentativa, ele salva {numero} pessoas")
        batman.append(numero)
        soma_batman += numero
        tentativas_batman -= 1

    print (f"\n=== {heroi[1]} dá uma volta na cidade e:\n")

    for i in range(tentativas_superman) :
        numero = randint(50, 100)
        print(f"Na sua {i+1}º tentativa, ele mata {numero} pessoas")
        superman.append(numero)
        soma_superman += numero
        tentativas_superman -= 1
    
    # Verificando a diferença de quantas pessoas salvas
    total_batman = (soma_batman - soma_superman)
    total_superman = (soma_superman - soma_batman)

    # Verificação de quem ganhou
    if soma_batman > soma_superman :
        return print (f"\n===== {heroi[0]} Salvou com {total_batman} pessoas a mais que o Superman =====")
    elif soma_superman > soma_batman :
        return print (f"\n===== {heroi[1]} Salvou com {total_superman} pessoas a mais que o Batman =====")
    else :
        return print (f"\n===== Empate =====")

# iniciando programa
competicao(heroi)