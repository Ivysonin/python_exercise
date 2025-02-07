# Dicionários
    # Utiliza index no formato de keys e values
    # Aceita string, integer, float, boolean...


# Dicionário para usar de exemplo
alunos = {'nome' : 'ivyson', 'idade' : '16'}


# Pega todas as chaves do dicionario
    # nesse exemplo: 'nome' , 'idade'
alunos.keys()


# Pega todos os valores do dicionario
    # nesse exemplo: 'ivyson' , '16'
alunos.values()


# Pega os pares (keys : values)
    # nesse caso: ('nome', 'ivyson'), ('idade', '16')
alunos.items()


# Copia de um dicionario para o outro
    # 'alunos1' recebe tudo que está dentro de 'alunos'
alunos1 = alunos.copy()


# Limpa o dicionario inteiro (deixa ele vazio)
alunos.clear()


# Pega o valor que está na chave (se NÃO houver a chave, pode exibir uma mensagem)
    # Exemplo: alunos.get('nota', 'Não tem nota')
alunos.get('nome')


# Adiciona ao final do dicionario uma ({keys : values})
    # pode atualizar o value se a key existir dentro do dicionario
    # pode adicionar mais de um
alunos.update({'nota' : 10})