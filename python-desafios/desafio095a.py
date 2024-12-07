jogador = dict()
partidas = list()
lista = list()
while True:
    jogador['nome'] = str(input('Nome do jogador: '))
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou: '))
    for c in range(1, tot + 1):
        partidas.append(int(input(f'Quantos gols fez na partida {c}: ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    resp = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    print('-:' * 22)
    if resp == 'N':
        break
lista.append(jogador.copy())
print(lista)
print(f'    {"cod":<7}{"Nome":<10}{"Gols":>7}{"Total":>10}')

    for p in lista:
        print(f'{c}{p['nome']}{p['gols']}{p['total']}')

"""
print('-:' * 22)

print('-:' * 22)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for i, v in enumerate(jogador['gols']):
    print(f'   ==> Na partida {i+1}, fez {v} gols.')
print('-:' * 22)
print(f'Foram um total de {jogador["total"]} gols.')"""

