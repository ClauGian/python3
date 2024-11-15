import random
n = random. randint(0, 5)
r = int(input('Escolha um número entre 0 e 5: '))
print('O número sorteado foi: ',n)
if r == n:
    print('Parabéns você acertou!')
else:
    print('infelizmente não foi desta vez.')


