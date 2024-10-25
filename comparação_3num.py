#           Comparação de três números consecutivos:
# Crie um programa que peça três números consecutivos
# ao usuário (um de cada vez) e verifique:

# Se os três números estão em ordem crescente, exiba a mensagem "Os números estão em ordem crescente".

#Se estão em ordem decrescente, exiba "Os números estão em ordem decrescente".

# Caso contrário, exiba "Os números não estão em ordem".

#            Regras:
# Utilize comparações com operadores relacionais para determinar a ordem dos números.

# Peça os três números individualmente e compare-os.

num1 = float(input ("Digite o primeiro número: "))
num2 = float(input ("Digite o segundo número: "))
num3 = float(input ("Digite o terceiro número: "))

if num1 < num2 and num2 < num3 :
    print ("Os números estáo em ordem crescente !")

elif num1 > num2 and num2 > num3 :
    print ("Os números estão em ordem decrescente !")

else:
    print ("Os números não estão em ordem !")