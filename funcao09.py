# Criar jogo de pedra,papel e tesoura
# J0gar com o conputador
# Se for empate começa uma nova jogada
###########################################################
from random import choice

# Jogo todo dentro da função 'jogo'
def jogo() :
    # Lista dos itens
    lista_escolhas = ["pedra", "papel", "tesoura"]

    while True :
        # Escolhendo o que vai jogar
        jogador = input ("=== Digite a opção: pedra, papel ou tesoura: ").lower()
        computador = choice(lista_escolhas) # 'choise' usado para pegar um item aleatoriamente da lista(tupla)
        
        # Organização
        print (f"=== O computador escolheu: {computador}")

        if jogador not in lista_escolhas :
            print ("\n===== ERRO, ESCOLHA CORRETAMENTE =====\n")
            continue

        # Se as escolhas for iguais o programa continua perguntando até não ser
        elif jogador == computador :
            print ("\n===== EMPATE! jogue novamente =====\n")

        elif ((jogador == "pedra" and computador == "tesoura") or
              (jogador == "papel" and computador == "pedra") or
              (jogador == "tesoura" and computador == "papel")) :
            mensagem = "\n===== Jogador venceu =====\n"
            return mensagem
        else:
            mensagem = "\n===== Computador venceu =====\n"
            return mensagem

# Iniciando jogo
print (jogo())