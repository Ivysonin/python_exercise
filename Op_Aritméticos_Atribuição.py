# Escreva um programa que peça ao usuário dois números inteiros. 
# Em seguida, realize as seguintes operações:

# Some os dois números
# Subtraia o segundo número do primeiro
# Multiplique os dois números
# Divida o primeiro número pelo segundo (lembre-se de lidar com divisão por zero)
# Exiba os resultados formatados.


num1 = int(input ("Digite um número: "))
num2 = int(input ("Digite outro número: "))
print ("================================")

# Está verificando se o num2 é diferente de 0(para poder fazer a divisão)
# Se for ele continua se não ele já para

if num2 != 0:
    result1 = num1 + num2
    result2 = num2 - num1
    result3 = num1 * num2
    result4 = num1 / num2
    print (f"Adição {num1} + {num2} = {result1}")
    print ("===============")
    print (f"Subtração {num2} - {num1} = {result2}")
    print ("===============")
    print (f"Multiplicação {num1} x {num2} = {result3}")
    print("===============")
    print (f"Divisão {num1} / {num2} = {result4:.2f}")
    print ("===============")

else:
    print ('Alguns operações não podem ser executadas causa do "0" !')