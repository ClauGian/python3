from argparse import PARSER
from random import randint

meu = soma = v = 0
parimpar = 'par'
res = 'impar'
print('==' * 20)
print('{:^40}'.format('VAMOS JOGAR PAR OU IMPAR'))
print('==' * 20)
while parimpar != res:
    meu = int(input('Qual é o seu valor: '))
    comp = randint(0, 10)
    soma = meu + comp
    parimpar = str(input('Par ou Impar: [P / I]: ')).upper().strip()
    print('..' * 20)
    if soma % 2 == 0:
        res = 'PAR'
    else:
        res = 'IMPAR'
    print(f'Você jogou {meu} e o computador {comp}.')
    print(f'O total deu {soma} → DEU {res}.')
    print('==' * 20)
    if parimpar == 'P' and res == 'PAR' or parimpar == 'I' and res == 'IMPAR':
        print('{:^40}'.format('Você VENCEU!!!'))
        print('{:^40}'.format('Vamos jogar novamente!'))
        print('==' * 20)
        v += 1
    else:
        print('{:^40}'.format('Você PERDEU!'))
        print('==' * 20)
        print(f'GAME OVER! Você venceu {v} vezes.')
        break



