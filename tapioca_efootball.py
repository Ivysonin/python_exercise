# CARDAPIO
ingrediente1 = "messi"
ingrediente2 = "neymar"
ingrediente3 = "cr7"
ingrediente4 = "haaland"
ingrediente5 = "valverde"

print ("====== Bem-vindo a tabiocaria eFootball ======\n")
print ("==== Aqui temos variedades de jogadores para vc escolher! ====")

tapioca_jogadores = []

while True:
    print ("Nossa lista de jogadores:\n")
    print ("1. Messi")
    print ("2. Neymar")
    print ("3. CR7")
    print ("4. Haaland")
    print ("5. Valverde\n")

    escolha = input ("Escolha de 1 a 5 ou digite sair para encerrar: ".lower())

    if escolha == "sair" :
        print ("Você encerrou suas escolhas !")
        break
    elif escolha == "1" :
        if ingrediente1 in tapioca_jogadores:
            print ("Esse Jogador já está, tente outro. \n")
        else:
            print ("Esse jogador foi adicionado ! \n")
            tapioca_jogadores.append(ingrediente1)
    elif escolha == "2" :
        if ingrediente2 in tapioca_jogadores:
            print ("Esse jogador já está, tente outro. \n")
        else:
            print("Esse jogador foi adicionado. \n")
            tapioca_jogadores.append(ingrediente2)
    elif escolha == "3" :
        if ingrediente3 in tapioca_jogadores:
            print ("Esse jogador já está, tente outro. \n")
        else:
            print("Esse jogador foi adicionado. \n")
            tapioca_jogadores.append(ingrediente3)
    elif escolha == "4" :
        if ingrediente4 in tapioca_jogadores:
            print ("Esse jogador já está, tente outro. \n")
        else:
            print ("Esse jogador foi adicionado. \n")
            tapioca_jogadores.append(ingrediente4)
    elif escolha == "5" :
        if ingrediente5 in tapioca_jogadores :
            print ("Esse jogador já está, tente outro. \n")
        else:
            print ("Esse jogador foi adicionado. \n")
            tapioca_jogadores.append(ingrediente5)
    else:
        print ("Você não está seguindo as instruções, Tente novamente.")

print ("Sua tapioca Efootball ficou assim: \n")

for ingredientes in tapioca_jogadores:
    print (f"- {ingredientes} \n")

print ("Obrigado por escolher a Tapiocaria eFootball !")