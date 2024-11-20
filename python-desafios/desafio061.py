print('\033[34m=' * 30)
print('{:^30}'.format('10 TERMOS DE UMA PA'))
print('\033[34m=\033[m' * 30)

t = int(input('Primeiro  Termo: '))
r = int(input('Informe a razão: '))
termo = t
c = 1
while c <= 10:
    print('\033[34m{}\033[m'.format(termo), end=' → ')
    termo += r
    c += 1
print('\033[33mAcabou!\033[m')

