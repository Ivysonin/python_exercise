# Desafio:
# Você recebeu uma lista com os seguintes nomes de cidades: ['Recife', 'Natal', 'Salvador', 'Fortaleza', 'João Pessoa'].
# Sua missão é ordená-los em ordem decrescente, ou seja, da letra mais “alta” na ordem alfabética para a mais “baixa”


lista_nome_cidade = ['Recife', 'Natal', 'Salvador', 'Fortaleza', 'João Pessoa']

lista_nome_cidade = sorted(lista_nome_cidade, reverse=True) # "True" reverte o padrão, deixando crescente em decrescente.

print(lista_nome_cidade)