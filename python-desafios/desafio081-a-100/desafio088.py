from random import randint
from time import sleep
lista = list()
jogos = list()
print()
print(':=' * 26)
print('{:^52}'.format('J O G O S   D A   M E G A - S E N A'))
print(':=' * 26)
print()
qtde = int(input('    Quantos jogos você quer que eu sorteie: '))
print()
tot = 1
while tot <= qtde:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('{:+^52}'.format(f'  SORTEANDO {qtde} JOGOS  '))
print()
for i, l in enumerate(jogos):
    sleep(1.3)
    print(f'    Jogo nº {i+1}: → {l}')
print()
print('{:=^52}'.format('  ← BOA SORTE!!! →  '))
