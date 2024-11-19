from random import randint
from time import sleep
c = 1
r = 0
n = ''
while c != (r == n):
    n = randint(1, 10)
    print('Estou pensando em um número entre 0 e 10. Tente adivinhar!')
    print('Qual foi o número que eu pensei?')
    r = int(input('\033[34mMeu Palpite é: \033[m'))
    sleep(0.3)
    print('.', end= '')
    sleep(0.3)
    print('.', end='')
    sleep(0.3)
    print('.', end='')
    sleep(0.3)
    print('.')
    if r != n:
        print('Infelizmente você ERROU! Tente novamente.')
        print('Eu pensei no número: {}'.format(n))
        print()
    else:
        print('\033[42mPARABÉNS!!! Você acertou!\033[m')
        print()
c = c + 1
print('Você tentou {} vezes.'.format(c))
