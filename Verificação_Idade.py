# Crie um programa que solicite ao usuário a idade e verifique 
# se a pessoa é menor de idade (menos de 18 anos), 
# maior de idade (entre 18 e 60 anos),
# ou idosa (mais de 60 anos). 
# O programa deve exibir uma mensagem apropriada para cada caso.

idade = int(input ("Digite sua idade: "))

if idade < 18 :
    print ("Você é menor de idade !")
elif 18 <= idade < 60 :
    print ("Você é maior de idade !")
else:
    print ("Você é idoso !")