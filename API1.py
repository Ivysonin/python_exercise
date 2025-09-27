'''
API gratuita que gera dados fictícios de pessoas
Site oficial: https://randomuser.me
'''


import requests

url = 'https://randomuser.me/api/'

resposta = requests.get(url)

if resposta.status_code == 200:
    dados = resposta.json()

    # Pegando dados
    user = dados["results"][0]
    genero = user["gender"]
    titulo = user['name']['title']
    nome = user["name"]["first"]

    print(f'Genero: {genero}') 
    print(f'Titulo: {titulo}') 
    print(f'Nome: {nome}')
else:
    print(f'ERRO:', resposta.status_code)