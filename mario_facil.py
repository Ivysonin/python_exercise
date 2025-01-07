#                          Exercício
# O usuário digita um número de 1 a 10, conforme o número, vai ser a quantidade de degraus 

while True:
    quantidade_degraus = int(input('\nDigite entre 1 e 8: ')) # Pedindo ao usuário um número

    if quantidade_degraus >= 1 and quantidade_degraus <= 8:
        # Pegando a quantidade e adicionando +1 para o indice ser oq o usuário digitar
        for i in range(quantidade_degraus+1): 

            # Os espaços vai ser multiplicado pela quantidade que o usuário digitou menos a variavel i (se o usuário digitou 5, então vai ter 4 espaços e o *)
            print(' ' * (quantidade_degraus-i) + '*' * i) 
        break