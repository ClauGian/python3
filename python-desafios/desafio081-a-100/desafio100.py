from random import randint
from time import sleep
sorte = []
vlr = 0
def sorteia(*num):
    print(f'Sorteando 5 valores da lista: ', end=' ')
    for c in range(1, 6):
        sorte.append(randint(1, 9))
    for i in sorte:
        sleep(0.5)
        print(f'{i} ', end=' ')
    print('→ Pronto!!!')
sorteia(sorte)

def somapar(vlr):
    for c in sorte:
        if c % 2 == 0:
            vlr += c
    sleep(1)
    print(f'Somando os valores pares de {sorte} temos um total de {vlr}.')

somapar(vlr)
