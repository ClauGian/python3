print('\033[34m=' * 30)
print('{:^30}'.format('TERMOS DE UMA PA'))
print('\033[34m=\033[m' * 30)

qt = int(input('Quantos Termos: '))
t = int(input('Primeiro  Termo: '))
r = int(input('Informe a razão: '))
dec = t + (qt - 1) * r
c = t
i = t
resp = ''
while c < dec + 1:
    print('{}'.format(c), end=' - ')
    c = c + r
resp = str(input('\nDeseja ver mais termos? [S / N] '))
if resp == 'S':
    n = int(input('Mais quantos termos deseja? '))
    qt = qt + n
    dec = t + (qt - 1) * r
    while i < dec + 1:
        print('{}'.format(i), end=' - ')
        i = i + r
print(' Fim.')





