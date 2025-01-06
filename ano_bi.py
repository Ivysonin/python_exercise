"""
A lógica de calcular se um ano é bissexto ou não é confusa, mas deu para entender um pouco

1. Se o ano é divisível por 4, ou seja, o resto da divisão é 0, ele continua com o processo.
Se não, o ano não é bissexto.

2. Se o ano é divisível por 100, ele continua o processo.
Se não, o ano é bissexto.

3. Se o ano é divisível por 400, o processo termina, e ele é declarado bissexto.
Se não, o ano não é bissexto
"""
def bissexto(ano):
    if ano % 4 == 0:
        if ano % 100 == 0:
            if ano % 400 == 0 :
                return 'É bissexto'
            else:
                return 'Não e bissexto'
        else:
            return 'É bissexto'
    else:
        return 'Não e bissexto'

# Perguntando o ano ao usuário
ano = int(input('\nAno: '))

# Mostrando o resultado do ano se É ou NÃO É bissexto
print(bissexto(ano))