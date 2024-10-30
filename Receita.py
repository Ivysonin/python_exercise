#                        EXERCICIO
# Desenvolva um programa em python que utilize tuplas para representar 
# os ingredientes e instruções dessa receita lendária. 
# Os participantes devem decifrar as tuplas e recriar o cuscuz ancestral 
# para desvendar seus segredos e saborear a autêntica tradição culinária. 
# O programa deve encerrar ao digitar 0 (zero)


# Tuplas de Ingredientes
ingrediente1 = ("Milho", "Farinha de milho")
ingrediente2 = ("Tomate", "Cebola", "Pimentão", "Coentro")
ingrediente3 = ("Água", "Sal", "Azeite")

ingredientes_escolhidos = [] # Lista para adicionar o que for escolhido

print ("====== RECEITA =====\n") # Organização
print ("====== Ingredientes :\n") # Organização
print ("1 - Milho, Farinha de milho") # Organização dos ingredientes
print ("2 - Tomate, Cebola, Pimentão, Coentro") # Organização dos ingredientes
print ("3 - Água, Sal, Azeite\n") # Organização dos ingredientes

while True :
    escolha = input ("=== Escolha entre 1 à 3 dos ingredientes acima (0 para sair): ")

    if escolha == "0" : # Ele PARA o loop
        break
    elif escolha == "1" :
        if ingrediente1 not in ingredientes_escolhidos : # Se não estiver adicionado ainda, ele adiciona
            ingredientes_escolhidos.append(ingrediente1)
        else: # Se já estiver, ele pula
            continue
    elif escolha == "2" :
        if ingrediente2 not in ingredientes_escolhidos : # Se não estiver adicionado ainda, ele adiciona
            ingredientes_escolhidos.append(ingrediente2)
        else: # Se já estiver, ele pula
            continue
    elif escolha == "3" :
        if ingrediente3 not in ingredientes_escolhidos : # Se não estiver adicionado ainda, ele adiciona
            ingredientes_escolhidos.append(ingrediente3)
        else: # Se já estiver, ele pula
            continue
    else: # Se o usuario digitar números diferente do que se pede, ou outras coisas
        print ("=== Você não está seguindo instruções !")

print ("\n===== Ingredientes escolhidos :\n") # Organização

contador = 1 # Para organizar loop abaixo
for i in ingredientes_escolhidos : # Listando ingredientes
    print (f"{contador} - {i}")
    contador += 1