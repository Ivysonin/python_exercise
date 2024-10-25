# Peça três números ao usuário e exiba qual deles é o maior.

num1 = int(input ("Número 1: "))
num2 = int(input ("Número 2: "))
num3 = int(input ("Número 3: "))

if num1 > num2 and num1 > num3 :
    print ("O Número 1 é maior que os outros !")
elif num2 > num1 and num2 > num3 :
    print ("O Número 2 é maior que os outros !")
elif num3 > num1 and num3 > num2 :
    print ("O Número 3 é maior que os outros !")
else:
    print ("Os números são iguais !")