# Escreva uma função que receba um número 
# e retorne True se ele estiver entre 10 e 20 (inclusive), e False caso contrário.

def recebe(numero): # não pensei em um nome melhor
    if numero in range(10,21):
        return True
    else:
        return False
    
numero = 21

print(recebe(numero))