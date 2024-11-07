#         EXERCICIO
# CALCULAR MÉDIA DE ALUNOS


# Criando função para calcular a média 
def calcular_media(nota1, nota2) :
    media = (nota1 + nota2) / 2
    return media

# Criando função para verificação
def status_aluno(media) :
    if media > 6 :
        print (f"\nAprovado! com média {media}")
    elif media >= 4 and media <= 6 :
        print (f"\nVerificação Suplementar! com média {round(media,2)}")
    elif media < 4 :
        print (f"\nReprovado! com média {media}")
    else:
        print ("\nErro!")

# Usuario escolhendo
nota1 = float(input ("Digite a primeira nota: "))
nota2 = float(input ("Digite a segunda nota: "))

# Adicionando a função a uma variavel
media = calcular_media(nota1, nota2)

# colocando a função de verificação para funcionar
status_aluno(media)