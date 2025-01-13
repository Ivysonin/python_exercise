# Um asterisco(*) siginifica que vai ter VÁRIOS argumentos como (1,2,3,4,5) 
# e UM parametro como (numeros)
def somar(*numeros):
    resultado = 0
    for i in numeros:
        resultado += i
    return resultado

soma_numero = somar(1,2,3,4,5)

print(f'Resuldado: {soma_numero}')