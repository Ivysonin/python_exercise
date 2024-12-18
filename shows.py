apresentacoes = [
    {"nome": "L7", "tipo": "música", "horario": "20:00", "local": "pátio do fórro"},
    {"nome": "alok", "tipo": "música", "horario": "22:00", "local": "pátio do fórro"},
    {"nome": "matue", "tipo": "música", "horario": "00:00", "local": "pátio do fórro"}
]

# A variavel 'indice' vai pegar todos os dicionarios que estão dentro da lista 'apresentacoes'
for indice in range(len(apresentacoes)) :
    # Pego os 3 dicionarios e acessando a chave 'nome/tipo' obtenho o valor
    print (f"Nome: {apresentacoes[indice]['nome']}, Tipo: {apresentacoes[indice]['tipo']}, Horarío: {apresentacoes[indice]['horario']}, Local: {apresentacoes[indice]['local']}")