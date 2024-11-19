n = int(input('Digite um número: '))
div = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[33m', end='')
        div += 1
    else:
        print('\033[34m', end='')
    print('{}\033[m'.format(c), end=' → ')
print('  FIM\n', end='')
if div == 2:
    print('O número {} possui apenas {} divisíveis. Portanto:'.format(n, div))
    print('O número\033[33m {} é PRIMO!\033[m'.format(n), end='')
else:
    print('O número {} possui {} divisíveis (mais que 2). Portanto:'.format(n, div))
    print('O número\033[34m {} NÃO É PRIMO!\033[m'.format(n), end='')
