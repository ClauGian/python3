jogador = dict()
partidas = list()
lista = list()
print('-:' * 30)
print(f'{"→ → →  CAMPEONATO PAULISTA  ← ← ←":^60}')
print('-:' * 30)
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou: '))
    partidas.clear()
    for c in range(1, tot + 1):
        partidas.append(int(input(f'Quantos gols fez na partida {c}: ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    lista.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
        if resp in 'SN':
            break
        print('ERRO! A Resposta dever ser S ou N.')
    if resp == 'N':
        break
print('-:' * 30)
print(f'   {"cod":<5} {"Nome":<10}{"Gols":>7}{"Total":>12}')
for k, v in enumerate(lista):
    print(f'    {k:<5}', end='')
    for d in v.values():
        print(f'{str(d):<13}', end='')
    print()
print('-:' * 30)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) Cod: '))
    if busca == 999:
        break
    if busca >= len(lista):
        print(f'ERRO! Não existe jogador com código {busca}.')
    else:
        print('-:' * 30)
        print(f'  → LEVANTAMENTO DO JOGADOR → {lista[busca]["nome"]}:')
        for i, g in enumerate(lista[busca]['gols']):
            print(f'    No jogo {i+1} fez {g} gols.')
print('-:' * 30)
print(f'{"  Encerrando... Volte Sempre!  ":=^60}')
print('-:' * 30)
