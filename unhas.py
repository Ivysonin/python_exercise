# Lista de serviços
LISTA_SERVICO = {
    1 : 'Aplicação',
    2 : 'Manutenção',
    3 : 'Blindagem',
    4 : 'Esmaltação em gel',
    5 : 'Blindagem + Esmaltação em gel',
    6 : 'Banho de gel (pés)',
    7 : 'Manutenção',
    8 : 'Remoção total'
}

# Lista de horários
LISTA_HORARIO = {
    1 : '13:00',
    2 : '15:30',
    3 : '18:00'
}

print('\n---------- NAIL DESIGNER ----------\n')

print('Por qual serviço você está procurando?\n')
print('[ 1 ] Aplicação')
print('[ 2 ] Manutenção')
print('[ 3 ] Blindagem')
print('[ 4 ] Esmaltação em gel')
print('[ 5 ] Blindagem + Esmaltação em gel')
print('[ 6 ] Banho de gel (pés)')
print('[ 7 ] Manutenção')
print('[ 8 ] Remoção total')

try:
    servico = int(input('Escolha um serviço (digite um número): '))

    print('\n---------- HORÁRIOS ----------\n')
    print('[ 1 ] 13:00')
    print('[ 2 ] 15:30')
    print('[ 3 ] 18:00')

    horario = int(input('Escolha o horário: '))

    if servico in [1,2,3,4,5,6,7,8] and horario in [1,2,3]:
        print('\n---------- AGENDAMENTO CONCLUÍDO ----------\n')

        print(f'Serviço escolhido: {LISTA_SERVICO.get(servico)}')
        print(f'Horário escolhido: {LISTA_HORARIO.get(horario)}')
        print('Ficamos na Rua Bananeira dos Cubos, número 13')
        print('Estou lhe aguardando!')

    else:
        print('\n---------- Você precisa escolher o serviço e o horário corretamente! ----------')

except ValueError:
    print('\n---------- Você não está seguindo instruções, reinicie e tente novamente ----------')
except:
    print('\n---------- ERRO, reinicie e tente novamente ----------')