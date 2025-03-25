# Importando biblioteca
import random


# Definindo cores usando sequência de escape ANSI
cor_ciano = '\033[1;36m'
cor_verde = '\033[1;32m'
cor_vermelho = '\033[31m'
reset_cor = '\033[0m' # Resetar a cor para o padrão


# Código
def main():
    print(f'\n{cor_ciano}========== UBER ==========\n{reset_cor}')
    # Escolhendo o local de viagem
    escolha_local = input(f'{cor_verde}Digite o nome da rua que deseja ir: {reset_cor}')

    try:
        # Escolhendo o veículo desejável
        escolha_veiculo = int(input(f'{cor_ciano}\nEscolha o número do veículo que deseja {reset_cor}'
                            '\n[ 1 ] Carro'
                            '\n[ 2 ] Moto'
                            '\n[ 3 ] Entrega Carro'
                            '\n[ 4 ] Entrega Moto'
                            f'{cor_verde}\n--- Digite sua escolha: {reset_cor}'))
        
        # Pegando um número inteiro aleátorio para servir de minutos
        tempo_estimado = random.randint(1,8)

        # Pegando um número aleátorio para servir de preço
        valores = random.randint(5, 20)

        # Verificação para a escolha do usuário ser entre 1 e 4
        if escolha_veiculo in [1, 2, 3, 4]:
            # Exibição
            print(f'\n{cor_ciano}Valor a ser pago: {valores}R${reset_cor}'
                f'\n\n{cor_ciano}Aguarde {tempo_estimado} minutos no local.{reset_cor}')
        else:
            raise ValueError
        
    except ValueError:
        print(f'\n{cor_vermelho}===== ERRO: digite um dos números apresentados =====\n{reset_cor}')
    except:
        print(f'\n{cor_vermelho}===== ERRO =====\n{reset_cor}')


# Executando programa
main()