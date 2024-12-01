from random import randint
par = 0
n = (randint(0, 10), randint(0, 10),
     randint(0, 10), randint(0, 10))
print(f'Os números são: {n}')
print(f'O valor 9 apareceu {n.count(9)} vezes.')
if 3 in n:
    print(f'O valor 3 apareceu na {n.index(3)+1}ª posição.')
else:
    print('O valor 3 não se encontra entre os números.')
print('Dentre os números acima, os valores pares são: ', end='')
for par in n:
    if par % 2 == 0:
        print(par, end=' ')
