print ("===== Derrote seu oponente =====")
hp_adversario = int(input ("Digite o hp do seu oponente: "))

# Enquanto o hp for maior que 0, o loop continua, no momento que não for, ele joga você para o if e o else da linha de código 17/19 !

while hp_adversario > 0:
    ataque = input ("Digite 'atacar' para causar dano no seu oponente: ")
    if ataque == "atacar" :
        dano = 10
        hp_adversario -= dano
        print (f"Você causou {dano} de dano. HP do oponente {hp_adversario}")
    else:
        break

# Se o oponente não 'atacou', ou parou de 'atacar', joga você para o else, se você continuou atacando e venceu, joga para o if !

if hp_adversario == 0:
    print ("===== Parabéns! Você derrotou seu oponente =====")
else:
    print ("===== Você não conseguiu, talvez na próxima ! =====")
