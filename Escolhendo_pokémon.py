# Tenho um dicionario aonde fica armazenado pokémons !
pokemon = {
    "1" : "Charmander",
    "2" : "Alakazam",
    "3" : "Pikachu"
    }

print ("===== POKÉMONS =====\n") # Organização

# Listando os pokémons !
contador = 1
for valor in pokemon.values() :
    print (f"{contador} - {valor}")
    contador += 1

escolha = input ("=== Escolha o pokémon digitando de 1 a 3: ")

# Verifica oque o usuario escolheu e manda uma mensagem !
if escolha == "1" :
    print (f"\n=== {pokemon["1"]} eu escolho você!") # Charmander
elif escolha == "2" :
    print (f"\n=== {pokemon["2"]} eu escolho você!") # Alakazam
elif escolha == "3" :
    print (f"\n=== {pokemon["3"]} eu escolho você!") # Pikachu
else:
    print ("\n=== Não está seguindo instruções, reinicie!")