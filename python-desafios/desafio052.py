n = int(input('Digite um número: '))
div = 0
for c in range(1, (n + 1)):
    if n % c == 0:
        div = div + 1
if div > 2:
    print('O número {} NÃO, é primo.'.format(n))
else:
    print('O número {} É PRIMO!'.format(n))


