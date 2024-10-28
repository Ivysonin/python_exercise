# Escolhendo jogadores secretos apenas digitando o número
#1- Utilizar dicionário para representar time lendario
#2- permitir que os participantes busquem combinar entre 1 a 5 elementos certos para criar o time
#3- para sair do programa o usuario deve digitar 0(zero)

# Dicionário
time = {
    1 : "Neymar" ,
    2 : "Messi" ,
    3 : "CR7" ,
    4 : "Haaland" ,
    5 : "Foden" 
    }

time_perfeito = {}

print ("====== Escolha Jogadores secretos ======\n") # Organização

qnt_jogadores = int(input ("=== Digite a quantidade de jogadores que deseja adicionar ao seu time(1 à 5): "))

for i in range(qnt_jogadores) :
    numero = input ("Digite o número do jogador secreto de 1 a 5 (0 para sair): ")
# Adicionando os jogadores conforme escolha do usuario
    if numero == "1" :
        time_perfeito.update({"Neymar" : numero}) # Neymar
    elif numero == "2" :
        time_perfeito.update({"Messi" : numero}) # Messi
    elif numero == "3" : 
        time_perfeito.update({"CR7" : numero}) # CR7
    elif numero == "4" :
        time_perfeito.update({"Haaland" : numero}) # Haaland
    elif numero == "5" : 
        time_perfeito.update({"Foden" : numero}) # Foden
    elif numero == "0" :
        break
    else:
        continue

print ("\n=== Jogadores escolhidos:\n") # Organização

contador = 1
for chave,valor in time_perfeito.items() :
    print(f"{contador} - {chave}")
    contador += 1

print(F"\n====== Parabéns Você Fez um Time Perfeito ======") # Organização