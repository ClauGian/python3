from random import randint
from time import sleep

sorteio = {}
números = list()
for j in range(1, 5):
    sorteio['jogador: 'f'{j}'] = randint(1, 6)
    números.append(sorteio.copy())
    sleep(1)
    print(f'O jogador {j} tirou {sorteio['jogador: 'f'{j}']}')
print()

print(sorteio)
print()

print(números[3])






