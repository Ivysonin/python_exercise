# Escreva um programa que tenha duas variáveis, idade e autorizacao.
# A variável idade deve ser um número inteiro e a variável autorizacao deve ser um valor booleano (True ou False).
# O programa deve verificar se a pessoa pode assistir a um filme, 
# com base na seguinte condição:

# Se a idade for maior ou igual a 18 ou a pessoa tiver autorização, o valor retornado deve ser True (pode assistir).
# Caso contrário, deve retornar False (não pode assistir).


# Troque os valores para testar
idade = 18
autorizacao = True

if idade >= 18 and autorizacao == True:
    print('Pode assistir (True)')
else:
    print('Não pode assistir (False)')