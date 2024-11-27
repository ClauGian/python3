
'''print('\033[34m=' * 30)
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
print(' Fim.') '''

print('\033[34m=' * 30)
print('{:^30}'.format('10 TERMOS DE UMA PA'))
print('\033[34m=\033[m' * 30)

t = int(input('Primeiro  Termo: '))
r = int(input('Informe a razão: '))
termo = t
c = 1
tot = 0
mais = 10
while mais != 0:
    tot = tot + mais
    while c <= tot:
        print('\033[34m{}\033[m'.format(termo), end=' → ')
        termo += r
        c += 1
    print('\033[33m Pausa...\033[m')
    mais = int(input('Quantos termos você quer exibir a mais? '))
print('\033[33mAcabou!!! \033[m')
print('Progressão finalizada com exibição de {} termos.'.format(tot))





