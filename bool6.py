# Use a expressão condicional (operador ternário: ) para verificar se um número n é positivo, negativo ou zero.
# Retorne uma string com o resultado ("Positivo", "Negativo", "Zero").

# formula:
# valor_se_verdadeiro if condicao else valor_se_falso


n = -1

resultado = 'Positivo' if n > 0 else 'Negativo' if n < 0 else 'zero'

print(resultado)