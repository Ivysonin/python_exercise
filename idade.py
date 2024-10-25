#       Comparação de idades:
#Crie um programa que peça a idade de duas pessoas 
# e informe quem é mais velho ou se as idades são iguais.

idade1 = int(input ("Digite a idade da pessoa1: "))
idade2 = int(input ("Digite a idade da pessoa2: "))

if idade1 > idade2 :
    print ("A pessoa1 é mais velha que a pessoa2 !")
elif idade1 < idade2 :
    print("A pessoa2 é mais velha !!")
else:
    print("Vocês tem a mesma idade !")