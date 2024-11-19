n = int(input('Quer o fatorial de qual número: '))
f = 1
c = n
while c > 0:
    f = f * c
    print('{}'.format(c), end=' x ')
    c = c - 1
print('\033[34m  → →\033[m ', end='')
print('  O Fatorial de {} é igual a {}.'.format(n, f))

print('{:=^30}'.format('Agora usando for'))

n = int(input('Quer o fatorial de qual número? '))
f = 1
for c in range(n, 0, -1):
    f = f * c
    print('{}'.format(c), end=' x ')
print('\033[34m  → →\033[m ', end='')
print('  O fatorial de {} é igual a:{}.'.format(n, f))
