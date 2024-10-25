salario_atual = float(input ("Me informe seu sálario atual: "))
print ("===================================")
#Usei uma fórmula que aprendi com gustavo guanabara: variavel +ou- (variavel * 0/100)

reajuste_20 = salario_atual + (salario_atual * 20/100) 
reajuste_15 = salario_atual + (salario_atual * 15/100)
reajuste_10 = salario_atual + (salario_atual * 10/100)
reajuste_5  = salario_atual + (salario_atual * 5/100)

#Conforme o aumento é menor, A forma como é falado muda.

if salario_atual <= 280.00 :
    print (f"O seu Sálario antes era de R${salario_atual}, Como você mostrou muito rendimento, Vamos da um aumento de 20% você agora passa a receber R${reajuste_20}")

elif salario_atual > 280.00 and salario_atual < 700.00 :
    print(f"O seu Sálario antes era de R${salario_atual}, Como você mostrou um rendimento, Vamos da um aumento de 15$ você agora passa a receber R${reajuste_15}")

elif salario_atual > 700.00 and salario_atual < 1500.00 :
    print (f"O seu Sálario antes era de R${salario_atual}, Como você está demonstrando desempenho, Vamos da um aumento de 10% você agora passa a receber R${reajuste_10}")
    
else:
    print (f"O seu Sálario antes era de R${salario_atual}, Como você trabalhou mais do que devia, vamos da um aumento de 5% você agora passa a receber R${reajuste_5}")
