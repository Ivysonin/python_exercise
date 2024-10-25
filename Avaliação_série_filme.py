#                EXERCICIO
# Você foi contratado(a) para desenvolver um programa de notas 
# da livreflix de N séries/filmes. O programa tem o nome 
# da série/filme e se a pessoa gostou, não gostou e amei. 
# Depois de inserir os dados exiba na tela 
# apenas os filmes/séries que a pessoa gostou ou amou

avaliacao = {} # Dicionário vazio

print ("===== Pesquisa sobre Séries e Filmes =====\n") # Organização

qnt_serie_filme = int(input ("=== Digite quantas avaliações quer fazer: ")) # usuario escolhe quantidade

print("") # organização

for i in range(qnt_serie_filme) :
    filme_serie = input ("Digite uma série ou filme: ")
    avaliar = input ("=== Para avaliar, G: para gostei, NG: para não gostei, A: para amei: ").upper() # 'upper' está transformando a resposta do usuario em maiúscula
    avaliacao.update({filme_serie : avaliar})

print ("") # organização

contador = 1
for chave,valor in avaliacao.items() :
    if valor == "G" or valor == "A" :
        print(f"{contador} - {chave}")
    contador +=1