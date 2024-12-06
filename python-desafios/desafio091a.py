from random import randint
itemgetter = 0
ranking = []
jogo = {'Jogador-1': randint(1, 6), 'Jogador-2': randint(1, 6), 'Jogador-3': randint(1, 6), 'Jogador-4': randint(1, 6)}
print('-*' * 15)
print(f'{"VALORES SORTEADOS":^30}')
print('--' * 15)
for k, v in jogo.items():
    print(f'    O {k} tirou → {v}')
print('-*' * 15)
print(f'{"RANKING DOS JOGADORES":^30}')
print('--' * 15)
for i in sorted(jogo, key = jogo.get, reverse=True):
    print(f'  º lugar: {i} com {jogo[i]}')


