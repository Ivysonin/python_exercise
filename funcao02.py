# Criar um programa que permitar o usuario escolher entre 3 camilhos diferentes
# fazer função para cada caminho
# encerrar ao digitar '0'

# Caminhos 1, 2 e 3
def caminho1() :
    print ("\n Você entrou na floresta para fazer um acampamento\n")

def caminho2() :
    print ("\n Você entrou no castelo e encontrou vários ossos muito raro\n")

def caminho3() :
    print ("\n Você entrou na caverna e encontrou várias pedras preciosas\n")

# Programa/sistema de escolha
def explorar() :
    while True :
    # Organização para escolha do usuario
        print("===== Caminhos para seguir =====\n")
        print ("1 - Floresta")
        print ("2 - Castelo")
        print ("3 - Caverna")
        print ("0 - Para finalizar")

        # Usuario fazendo escolha
        escolha = int(input ("\n=== Digite o caminho que deseja seguir: "))

        # Analisando a escolha do usuario e exibido conforme
        if escolha == 0 :
            print ("\n=== Você encerrou o programa ===")
            break
        elif escolha == 1 :
            caminho1()
        elif escolha == 2 :
            caminho2()
        elif escolha == 3 :
            caminho3()
        else:
            print ("\n===== ERRO, tente de novo =====\n")

# Executando programa
explorar()