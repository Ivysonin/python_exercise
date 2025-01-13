# Default = aquele que você define o valor no parametro
# Non-default = aquele que você NÃO define o valor no parametro

def multiplicar(num1, num2=2): # Usando Default no paremetro 'num2'
    return f'{num1} x {num2} = {num1 * num2}'

num1 = int(input('Digite um número:'))
num2 = int(input('Digite um número:'))

print(multiplicar(num1, num2))
# OU
# print(multiplicar(num1))