print ("========== Calculando a Média ==========")

nota1 = float (input ("Digite sua nota de AT: "))
nota2 = float (input ("Digite sua nota da Prova: "))
media = (nota1 + nota2) / 2

if media == 10 :
    print (f"Sua média {media}. Você está aprovado, Párabens você é um aluno excelente <3")
    print ("====================")
elif media >= 7 and media != 10 :
    print (f"Sua média {media}. Você está aprovado !")
    print ("====================")
else:
    print (f"Sua média {media}. Você está em recuperação, estude mais ! ")
    print ("====================")
