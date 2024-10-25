# Escreva um programa que peça ao usuário para adivinhar 
# um número secreto (que você definirá no código). 
# O programa deve permitir que o usuário tente até acertar 
# mas se ele digitar um número negativo, o programa deve parar 
# imediatamente com a mensagem "Adivinhação interrompida".

numero_secreto = 10

while True:
    palpite = int(input ("Digite seu palpite: "))

    if palpite < 0:
        print ("Adivinhação interrompida")
        break
    elif palpite == numero_secreto:
        print ("Parabéns!você acertou")
        break
    else:
        print ("tente novamente")