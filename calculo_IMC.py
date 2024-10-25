# Faça um programa que receba o peso e a altura de uma pessoa 
# e calcule o Índice de Massa Corporal (IMC). 
# Exiba também uma mensagem dizendo se a pessoa está abaixo do peso
# no peso ideal ou acima do peso, usando a seguinte tabela:
#      TABELA
#Abaixo de 18.5: Abaixo do peso
#Entre 18.5 e 24.9: Peso normal
#Entre 25 e 29.9: Sobrepeso
#30 ou mais: Obesidade

peso = float(input ("Digite seu peso: "))
altura = float(input ("Digite sua altura: "))
massa_corporal = peso / (altura**2) # Formula para calcular IMC

if massa_corporal < 18.5 :
    print (f"Com o IMC de {massa_corporal:.2f}, você está abaixo do peso !")

elif massa_corporal >= 18.5 and massa_corporal <= 24.9 :
    print (f"Com o IMC de {massa_corporal:.2}, Seu peso está ideal !")

elif massa_corporal >= 25.0 and massa_corporal <= 29.9 :
    print (f"Com o IMC de {massa_corporal:.2f}, você está Sobrepeso, começe a se cuidar !")

else:
    print (f"Com o IMC de {massa_corporal:.2f} Você está com obesidade, precisa se cuidar ")