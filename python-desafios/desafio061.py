print('\033[34m=' * 30)
print('{:^30}'.format('10 TERMOS DE UMA PA'))
print('\033[34m=\033[m' * 30)

t = int(input('Primeiro  Termo: '))
r = int(input('Informe a razão: '))
dec = t + (10 - 1) * r
c = t
while c < dec + 1:
    print('\033[34m{}\033[m'.format(c), end=' → ')
    c = c + r
print('\033[33mAcabou!\033[m')

