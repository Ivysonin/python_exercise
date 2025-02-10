# Lambda Function
    # É uma função (pequena) sem nome
    # Pode ter vários argumentos mas somente 1 expressão
    # Código mais 'clean'
    # Usado dentro de outras funções


# Pegando um número adicionando mais 10 a ele e depois multiplicando por 10
def multiplicar(num: int) -> int:
    atribuindo10 = lambda x: x + 10
    return atribuindo10(num) * 10


numero = int(input('Digite um número: '))

# Realizando cálculos da esquerda para direita
print(f'{numero} + 10 x 10 = {multiplicar(numero)}')