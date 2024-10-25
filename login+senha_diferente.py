# Iniciando

print ("======== Bem-Vindo, faça seu cadastro! ========")
login = input ("Digite seu login: ")
senha = input ("Digite sua senha: ")

# Colocando limetes para tentar

max_tentativas = 3
tentativas = 0

# O loop só vai para, se as tentativas atingir o limete, ou se fizer o cadastro de maneira certa.

while login == senha :
    if tentativas != max_tentativas :
        print ("ERRO, seu login e senha são iguais,tente novamente !")
        login = input ("Digite seu login: ")
        senha = input ("Digite sua senha: ")
        tentativas +=1
    else:
        print ("===== Você atingiu o máximo de tentativas =====")
        break

# Se atingir o máximo de tantativas joga para o else porque
# o login e a senha vão ser iguais.
# Se não, o login e a senha vão ser diferentes, jogando para o if.

if login != senha :
    print ("====== Conta Criada com sucesso ======")
else:
    print ("===== Volte depois de 10 minutos =====")