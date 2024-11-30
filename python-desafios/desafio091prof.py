from random import randint
from time import sleep
from operator import itemgetter
jogo = {'jogador 1': randint(1, 6),
        'jogador 2': randint(1, 6),
        'jogador 3': randint(1, 6),
        'jogador 4': randint(1, 6)}
ranking = list()
print('-.' * 15)
print(f'{" VALORES SORTEADOS ":=^30}')
print('-.' * 15)
for k, v in jogo.items():
    sleep(1.3)
    print(f' - {k} tirou {v} no dado.')
print(f'{" RANKING DOS JOGADORES ":=^30}')
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    sleep(1)
    print(f' - {i+1}º lugar: {v[0]} com {v[1]}.')
print('-.' * 15)