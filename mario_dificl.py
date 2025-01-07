# Com a base que uma escada do mario foi feita,
# Faça duas escadas, uma do lado da outra.
# Pergunte ao usuário o tamanho da escada.

while True:
    quantidade_degraus = int(input('\nDigite entre 1 a 8: '))

    if 1 <= quantidade_degraus <= 8:
        for i in range(quantidade_degraus+1):
            #              DUAS PARTES
            # 1. Os espaços vai ser multiplicado pela quantidade que o usuário digitou menos a variavel i (se o usuário digitou 5, então vai ter 4 espaços e o *) 
            # +
            # 2. O espaçamento '    ' e a lógica padrão para exibir a escadinha '*' * i
            print(' ' * (quantidade_degraus - i) + '*' * i + '    ' + '*' * i)
        break
""" A fórmula simples para fazer uma escadinha padrão:

    for i in range(quantidade_degraus+1):
        print('*' * i)

"""