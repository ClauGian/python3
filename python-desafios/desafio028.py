from random import randint
from time import sleep
n = randint(0, 5)
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar!')
print('-=-' * 20)
r = int(input('Qual foi o número que eu pensei? '))
print('PROCESSANDO...')
sleep(3)
if r == n:
    print('Parabéns você ACERTOU!')
    print('Eu também pensei no número: {}.'.format(n))
else:
    print('Infelizmente você ERROU.')
    print('Eu pensei no número: {}.'.format(n))