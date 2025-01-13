# Dois asterisco(**) siginifica que vai ter VÁRIOS argumentos
# E vou poder definir os parametros quando definir os argumentos
def agencia(**carro):
    return carro

# Parametros: marca, cor, motor, placa
# Argumentos: 'BMW', 'Branco', '100', '1234'))
print(agencia(marca='BMW', cor='Branco', motor='100', placa='1234'))
print(agencia(marca='BMW', cor='Vermelho', motor='100'))
print(agencia(marca='BMW', cor='Preto'))