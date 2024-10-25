# Escreva um programa que solicite ao usuário uma sequência de números. 
# O programa deve imprimir a soma de todos os números positivos que o usuário inserir. 
# Se o usuário inserir um número negativo, ele deve ser ignorado (use continue)
# e o programa deve pedir outro número.
# O programa para de pedir números quando o usuário insere 0 (use break).

soma = 0

while True:
    numeros = int(input ("Digite um número (0 para sair): "))

    if numeros < 0:
        continue
    elif numeros == 0:
        break

    soma += numeros

print (f"Seus números somados {soma} !")