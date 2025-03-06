'''
Soma dos Dígitos: 
Escreva uma função que receba um número inteiro e retorne a soma de seus dígitos'
'''


def somaDigito(num: int) -> int:
    num = str(num) # Convertendo para conseguir dividir os números
    soma = 0
    for i in num:
        i = int(i)
        soma += i
    return soma


# Pegando o número do usuário
numero = int(input('Digite um número grande(Exemplo: 253): '))

# Pegando o resultado
resultado = somaDigito(numero)

# Exibindo o resultado
print(f'A soma de {numero} é: {resultado}')