'''
Crie uma função chamada artifact_locatorque receba artifact_name como parâmetro.

Esta função tem como objetivo ajudar um amigo a navegar 
pelo peculiar sistema de ordenação de artefatos de um museu.
O museu agrupa os artefatos pela primeira letra e os coloca
em ordem alfabética dentro desses grupos. 
No entanto, eles se esqueceram de colocar placas para cada grupo.

Dado o nome do artefato que seu amigo deseja ver, a função deve retornar uma string que inclui:

A primeira letra do nome do artefato (representando o grupo).
O próprio nome do artefato.
Por exemplo, se a entrada for "Mona Lisa", 
a função deve retornar "M - Mona Lisa". 
Dessa forma, seu amigo pode navegar facilmente para 
o grupo 'M' e então encontrar a "Mona Lisa" dentro desse grupo.

Parâmetros:

artifact_name(str): O nome do artefato que seu amigo quer encontrar.
A função retorna uma string que combina a primeira letra do nome do artefato e o próprio nome do artefato, separados por um traço e um espaço.
'''

def artifact_locator(artifact_name : str) -> str:
    return f'{artifact_name[0].upper()} - {artifact_name}'

nome_do_artefato = 'Mona lisa'

print(artifact_locator(nome_do_artefato))