# Importando a classe Flask
from flask import Flask

# Criando a aplicação Flask
app = Flask(__name__)

# Definindo a rota para a URL raiz "/"
@app.route('/', methods=['GET'])
def ola_mundo():
    return 'Olá, mundo! <3'

# Executando no modo debug para recarregar automaticamente em mudanças no código
app.run(debug=True)