# Função criada para armanezar as histórias dos jogadores
def historia(escolha):
    match escolha:
        case '1':
            print('\nMessi: Considerado um dos maiores da história, é um maestro em campo com visão, gols e assistências, colecionando troféus e recordes ao longo de sua brilhante carreira.\n')
        case '2':
            print('\nNeymar: Ícone do futebol brasileiro, combina habilidade técnica, dribles ousados e carisma, conquistando títulos importantes por clubes e seleção.\n')
        case '3':
            print('\nCristiano Ronaldo: Reconhecido pela dedicação, poder físico e instinto goleador, é um exemplo de longevidade no futebol, com feitos históricos por clubes e seleções.\n')

# Iniciando programa
escolha_historia = input('------ Resumo ------\n'
                         'Falando um pouco da vida de cada jogador a seguir:\n'
                         '[ 1 ] Messi\n'
                         '[ 2 ] Neymar\n'
                         '[ 3 ] Cristiano ronaldo\n'
                         'Escolha apenas um número: ')

# Fazendo verificação de valores digitados pelo usuário
if escolha_historia == '1' or escolha_historia == '2' or escolha_historia == '3' :
    # Imprimindo a escolha do usuario
    historia(escolha_historia)
else:
    print('\nERRO: escolha o número entre 1 e 3\n')