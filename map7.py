# Exercício: calculando o imposto de produtos
    # Fórnmula para calcular: valor + (valor * porcentagem/100)


produtos = [1200, 187.90, 18]

valor_com_imposto = list(map(lambda x: x + (x * 10/100), produtos))

print(f'Preço original do produto: {produtos}')
print(f'Preço com imposto de 10%: {valor_com_imposto}')