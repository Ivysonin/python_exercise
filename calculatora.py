print ("============ CALCULATORA ============")

# Colocando variaveis de escolha !

adicao = "+"
subtracao = "-"
multiplicacao = "x"
divisao = "/"
operacao = input ("Escolha um operador: (+, x, - e / : ")

# Executando o que eu escolhi !

# SOMANDO 
if operacao == adicao :
    print ("===== SOMANDO =====")
    num1 = int(input ("Digite um número: "))
    num2 = int(input ("Digite outro número: "))
    print (f"A soma de {num1} + {num2} = {num1 + num2}")

# SUBTRAINDO
elif operacao == subtracao:
    print ("===== SUBTRAINDO =====")
    num3 = int(input ("Digite um número: "))
    num4 = int(input ("Digite outro número: "))
    print (f"A subtração de {num3} - {num4} = {num3 - num4}")

# MULTIPLICANDO
elif operacao == multiplicacao:
    print ("===== MULTIPLICAÇÃO =====")
    num5 = int(input ("Digite um número: "))
    num6 = int(input ("Digite outro número: "))
    print (f"A multiplicação de {num5} x {num6} = {num5 * num6}")

# DIVIDINDO
elif operacao == divisao:
    print ("===== DIVISÃO =====")
    num7 = float(input ("Digite um número: "))
    num8 = float(input ("Digite outro número: "))
    print (f"A divisão de {num7:.0f} / {num8:.0f} = {num7 / num8:.1f}")

# NÃO SEGUIU INSTRUÇÕES
else:
    print ("===== Você não está seguindo as instruções =====")
