from random import randint
from time import sleep
print('{:-^30}'.format('\033[34m J O   K E N   P O \033[m'))
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print(''' Suas Opções:
 [ 0 ] PEDRA
 [ 1 ] PAPEL
 [ 2 ] TESOURA ''')
eu = int(input('\033[32m Qual é a minha Jogada:\033[m '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('\033[32m-=\033[m'* 15)
print('\033[31mComputador........= {}\033[m'.format(itens[computador]))
print('\033[1;34mJogador "EU"......= {}\033[m'.format(itens[eu]))
print('\033[32m-=\033[m'* 15)

if computador == 0:
    if eu == 0:
        print('Empatou')
    elif eu == 1:
        print('\033[1;34mEU venci\033[m')
    elif eu == 2:
        print('\033[31mComputador Venceu\033[m')
    else:
        print('JOGADA INVÁLIDA')
elif computador == 1:
    if eu == 0:
        print('\033[31mComputador Venceu\033[m')
    elif eu == 1:
        print('Empatou')
    elif eu == 2:
        print('\033[1;34mEU venci\033[m')
    else:
        print('JOGADA INVÁLIDA')
elif computador == 2:
    if eu == 0:
        print('\033[1;34mEU venci\033[m')
    elif eu == 1:
        print('\033[31mComputador Venceu\033[m')
    elif eu == 2:
        print('Empatou')
    else:
        print('JOGADA INVÁLIDA')
