# Crie uma função chamada calcula_desconto que receba dois parâmetros:

# preco_original - o preço original de um produto.
# desconto - a porcentagem de desconto a ser aplicada, com valor padrão de 10%.

# A função deve retornar o preço com o desconto aplicado. 
# Depois, chame a função com e sem o valor do desconto para testar.

def calcula_desconto(preco_original, desconto=10) -> int :
    # Fórnmula: valor - (valor * porcentagem/100)
    return preco_original - (preco_original * desconto/100) 

# Sem o segundo parâmetros
print(calcula_desconto(200))

# Com os dois parâmetros
print(calcula_desconto(200, 20 ))