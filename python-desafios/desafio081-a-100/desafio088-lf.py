from random import randint
from time import sleep
lista = list()
jogos = list()
print()
print(':=' * 35)
print('{:^70}'.format('J O G O S   D A   L O T O - F A C I L'))
print(':=' * 35)
print()
qtde = int(input('        Quantos jogos você quer que eu sorteie: '))
print()
tot = 1
while tot <= qtde:
    cont = 0
    while True:
        num = randint(1, 25)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 15:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('{:+^70}'.format(f'  SORTEANDO {qtde} JOGOS  '))
print()
for i, l in enumerate(jogos):
    sleep(1.3)
    print(f'Jogo nº {i+1}: → {l}')
print()
print('{:=^70}'.format('  ← BOA SORTE!!! →  '))
