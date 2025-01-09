class Criar_coracao:
    def __init__(self, tamanho):
        self.coracao = tamanho

    def exibir_coracao(self):
        # PARTE SUPERIOR DO CORAÇÃO
        if self.coracao == 6: # Tamanho do coração
            contador = 2
            for i in range(contador):
                espaco_inicial = '  ' if i == 1 else '   ' # Manipulando os espaços para alinhar os asteriscos
                canto_esquerto = '*' * 4 if i == 1 else '*' * 2 # Quando o valor de 'i' for 1 ele coloca 4 asterisco se não for ele coloca apenas 2
                espaco_central = ' ' if i == 1 else '   '
                canto_direito = '*' * 4 if i == 1 else '*' * 2
                print(cor_vermelho + espaco_inicial + canto_esquerto + espaco_central + canto_direito)
        elif self.coracao == 7: # Tamanho do coração
            contador = 2
            for i in range(contador):
                espaco_inicial = '  ' if i == 1 else '   ' # Manipulando os espaços para alinhar os asteriscos
                canto_esquerto = '*' * 5 if i == 1 else '*' * 3 # Quando o valor de 'i' for 1 ele coloca 5 asterisco se não for ele coloca apenas 3
                espaco_central = ' ' if i == 1 else '   '
                canto_direito = '*' * 5 if i == 1 else '*' * 3
                print(cor_vermelho + espaco_inicial + canto_esquerto + espaco_central + canto_direito)

        # PARTE INFERIOR DO CORAÇÃO
        for i in range(self.coracao-2, -1, -1): 
            print(f'{cor_vermelho} ' * (self.coracao - i) + '*' * i + '*' * i + f'*{reset_cor}')

# Definindo cores usando sequência de escape ANSI
cor_ciano = '\033[1;36m'
cor_verde = '\033[1;32m'
cor_vermelho = '\033[31m'
reset_cor = '\033[0m' # Resetar a cor para o padrão

try:
    # Pegando o tamanho do coração
    tamanho_coracao = int(input(f'\n{cor_verde}Escolha o tamanho do coração [6, 7]: {reset_cor}'))
# Lidando com erros do usuário
except ValueError:
    print(f"\n{cor_vermelho}ERRO: digite números inteiros{reset_cor}")
except:
    print(f'\n{cor_vermelho}ERRO: não identificado{reset_cor}')

if tamanho_coracao in [6, 7]:
    coracao = Criar_coracao(tamanho_coracao)
    coracao.exibir_coracao()
else:
    print(f"\n{cor_vermelho}ERRO: Digite o número [6, 7]{reset_cor}")