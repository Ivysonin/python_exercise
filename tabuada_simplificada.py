print ("===== Escolha um número e veja sua tabuada =====")
numero = int(input ("Digite um número: "))
contador = 1

# O loop ele para causa do contador, na linha 7 se em vez de 'contador' fosse 'numero', entraria em um loop infinito !

while contador <= 10:
    resultado = numero * contador
    print (f"{numero} x {contador} = {resultado}")
    contador +=1
