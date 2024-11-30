jogador = dict()
partidas = list()
jogador['nome'] = str(input('Nome do jogador: '))
tot = int(input(f'Quantas partidas {jogador["nome"]} jogou: '))
for c in range(1, tot + 1):
    partidas.append(int(input(f'Quantos gols fez na partida {c}: ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)

print('-:' * 22)
print(jogador)
print('-:' * 22)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor: {v}.')
print('-:' * 22)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for i, v in enumerate(jogador['gols']):
    print(f'   ==> Na partida {i+1}, fez {v} gols.')
print('-:' * 22)
print(f'Foram um total de {jogador["total"]} gols.')

