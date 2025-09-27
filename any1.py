'''
A função any() retorna True se pelo menos um elemento de um iterável for verdadeiro.
Caso contrário, retorna False
'''

# Verificando presença de números positivos
numeros = [-3, -2, -1, 0, 1, 2, 3]

resultado = any(n > 0 for n in numeros)

print(resultado)