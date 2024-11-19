print('\033[34m=' * 30)
print('{:^30}'.format('10 TERMOS DE UMA PA'))
print('\033[34m=\033[m' * 30)
n = int(input('Primeiro termo: '))
r = int(input('Razão: '))
dec = n + (10 - 1) * r # Para mostrar 10 termos(formula matemática)
for c in range(n, dec + 1, r):
    print('{}'. format(c), end= ' → ')
print('Acabou!')
