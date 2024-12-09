from time import sleep
def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print(f'    Contagem de {i} até {f} de {p} em {p}.')
    sleep(1)
    if i < f:
        cont = i
        while cont <= f:
            sleep(.5)
            print(f'  {cont}', end=' ')
            cont += p
        print(' Fim!')
    else:
        cont = i
        while cont >= f:
            sleep(.5)
            print(f'  {cont}', end=' ')
            cont -= p
        print(' Fim!')
    print('~.' * 24)
print('~.' * 24)
print(f'{"Contando com Python":^48}')
print('~.' * 24)
contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é sua vez de personalizar a contagem!')
ini = int(input('Inicio: '))
fim = int(input('Fim...: '))
pas = int(input('Passo.: '))
contador(ini, fim, pas)

