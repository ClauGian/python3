from time import sleep
print('-=' * 24)
def contador(inicio, fim, passo):
    if inicio > fim:
        passo = (passo * -1)
    if passo == 0:
        passo = 1
    for c in range(inicio, fim+passo, passo):
        sleep(.5)
        print(f'  {c}', end=' ')
    print(' → Fim.')
print('  Contagem de 1 até 10 de 1 em 1:')
contador(1, 10, 1)
print('-=' * 24)
print('  Contagem 10 a 0 de 2 em 2:')
contador(10, 0, 2)
print('-=' * 24)
print('  Agora é sua vez de personalizar a contagem!')
i = int(input('  Inicio: '))
f = int(input('  Fim: '))
p = int(input('  Passo: '))
contador(i, f, p)
print('-=' * 24)
print(f'{"Acabou!!!":^48}')

