from random import randint
from time import sleep

def sorteia(lista):
    print('Sorteando 5 valores da lista: →  ', end='')
    for cont in range(0, 5):
        n = randint(0, 9)
        lista.append(n)
        sleep(.5)
        print(f'{n}', end='  ')
    print('→ Pronto!')

def somapar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'A soma dos valores pares de {lista} é igual a: {soma}.')

números = list()
sorteia(números)
somapar(números)