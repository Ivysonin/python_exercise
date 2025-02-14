'''
Crie um programa em Python
que converta uma lista de temperaturas de Celsius 
para Fahrenheit usando a função map
'''

# fórmula para calcular: f = (c * 9/5) + 32

temperaturas_celsius = [0, 20, 30, 40, 100]

fahrenheit = list(map(lambda c: (c * 9/5) + 32, temperaturas_celsius))

print(f'Temperaturas em Celsius: {temperaturas_celsius}')
print(f'Temperaturas em Fahrenheit: {fahrenheit}')