from random import randint
from time import sleep
'''
                        Minha versão.
c = 1
r = 0
n = ''
palpites = 0
while c != (r == n):
    n = randint(1, 10)
    print('Estou pensando em um número entre 0 e 10. Tente adivinhar!')
    print('Qual foi o número que eu pensei?')
    r = int(input('\033[34mMeu Palpite é: \033[m'))
    palpites += 1
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
print('Você tentou {} vezes.'.format(palpites))
                
                versão do prof.
'''
computador = randint(0, 10)
print('Olá, sou o computador. Acabei de pensar em um número entre 0 e 10')
print('Será que você consegue adivinhar qual foi?')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        elif jogador > computador:
            print('Menos... Tente mais uma vez.')
print('Acertou com {} tentativas. PARABÉNS.'.format(palpites))

