from random import randint
from time import sleep
from operator import itemgetter

ranking = []
jogo = {'Jogador-1': randint(1, 6), 'Jogador-2': randint(1, 6),
        'Jogador-3': randint(1, 6), 'Jogador-4': randint(1, 6)}
print('-*' * 15)
print(f'{"VALORES SORTEADOS":^30}')
print('--' * 15)
for k, v in jogo.items():
    sleep(1)
    print(f'    O {k} tirou → {v}')
print('-*' * 15)
print(f'{"RANKING DOS JOGADORES":^30}')
print('--' * 15)
ranking = sorted(jogo.items(), key = itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    sleep(1)
    print(f' → {i+1}º lugar: {v[0]} com {v[1]}')


