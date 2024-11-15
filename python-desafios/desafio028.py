from random import randint
from time import sleep
n = randint(0, 5)
print('\033[1;30;42m-=-\033[m' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar!')
print('\033[1;30;42m-=-\033[m' * 20)
r = int(input('Qual foi o número que eu pensei? '))
print('\033[35mPROCESSANDO...\033[m')
sleep(3)
if r == n:
    print('\033[30;43mParabéns você ACERTOU!\033[m')
    print('Eu também pensei no número: {}.'.format(n))
else:
    print('\033[31mInfelizmente você ERROU.\033[m')
    print('Eu pensei no número: {}.'.format(n))