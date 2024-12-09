from random import randint
from time import sleep
print()
print('-*' * 23)
print(f'{"JOGOS DA LOTOMANIA":^46}')
print('-*' * 23)
jogos = []
lista = []
qt = 0
tot = 1
qt = int(input('       Quantos jogos você quer gerar: '))
print('-' * 46)
print(f'{f"----> GERANDO {qt} JOGOS <----":^46}')
print()
while tot <= qt:
    cont = 0
    while True:
        palpite = randint(1, 100)
        if palpite not in lista:
            lista.append(palpite)
            cont += 1
        if cont >= 50:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
for i, l in enumerate(jogos):
    sleep(1.2)
    print(f'     Jogo nº {i+1}  →  {l}')
print()
print(f'{"> Boa Sorte! <":-^46}')






