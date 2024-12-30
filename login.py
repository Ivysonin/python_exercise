class Cadastro:
    def __init__(self, usuario, email, senha):
        self.usuario = usuario
        self.email = email
        self.senha = senha

    def informacoes(self):
        print(f"\nUsuário: {self.usuario}\n"
              f"E-mail: {self.email}\n"
              f"Senha: {self.senha}")

# Inicializando variavel fora do loop para não causar um erro de variavel não existente
criar_cadastro = None 

# Para salvar e exibir os cadastros que vão ser feitos por usuários
banco_de_dados = [] 

print ("===== CADASTRO =====") # Organização
while True:
    # Fazendo as escolhas
    escolha = input("\nDeseja se cadastrar? (Digite o número correspondente)\n"
                    "[ 1 ] Cadastrar\n"
                    "[ 2 ] Verificar Todos os Cadastro\n"
                    "[ 3 ] Encerrar\n"
                    "===== Escolha: ")

    # Encerrando programa
    if escolha == '3': 
        print ("\n===== Programa encerrando... =====\n")
        break

    # Exibindo informações de cadastros
    elif escolha == '2': 
        if len(banco_de_dados) > 0: # Verificando se tem cadastro feito, se sim:
            print ("\n===== CADASTROS =====")
            for contas in banco_de_dados: # Pegando cada instância dentro da lista e exibindo com 'informacoes()'
                contas.informacoes() # Mesmo sendo uma função da classe eu posso usar, dependendo do contexto pode ser uma boa prática(mas não é tão recomendada)
        else: # se não:
            print("\nERRO: faça primeiro um cadastro =====")

    # Cadastrando usuários
    elif escolha == '1':
        usuario = input ("Digite seu nome de Usuário: ")
        email = input ("Digite seu E-mail: ")
        senha = input ("Digite sua Senha: ")

        print ("\n==== Cadastro realizado! =====")
        criar_cadastro = Cadastro(usuario, email, senha) # Variavel 'criar_cadastro' deixando de ser um valor None e se tornando uma instância da classe 'Cadastro'
        
        # Adicionando ao 'banco_de_dados' a instância 'criar_cadastro' 
        banco_de_dados.append(criar_cadastro) 

    # Escolha diferente dos números apresentados
    else: 
        print("\n=====ERRO: escolha os números 1, 2 ou 3 =====")