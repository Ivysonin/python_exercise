# importando uma bibliotaca

import random #aleátorio
numero_secreto = random.randint (1,100)
tentativas = 1

print ("\n===== Tentando acertar um número secreto entre (1,100) =====\n")
palpite = int(input ("Digite um palpite: "))

# Sistema de loop até acerta o número correto 

while palpite != numero_secreto:
    print ("===== Você não acertou o número, tente novamente =====\n")
    if palpite < numero_secreto:
        print ("Dica: O número é maior !")
    else:
        print ("Dica: O número é menor !")
    palpite = int(input ("Digite um palpite: "))
    tentativas += 1

print (f"\n========== Parabéns! Você acertou em {tentativas} tentativas, O número secreto é {numero_secreto} ==========")