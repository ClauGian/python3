jogador = dict()
partidas = list()
times = list()
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou: '))
    partidas.clear()
    for c in range(1, tot + 1):
        partidas.append(int(input(f'Quantos gols fez na partida {c+1}: ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    times.append(jogador.copy())
    while True:
        resp = str(input('Deseja continuar? [S/N]: ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! A resposta deve ser S ou N.')
    print('-:' * 22)
    if resp == 'N':
        break

print('-:' * 22)
print('Cod ', end='')
for i in jogador.keys():
    print(f'{i:<11}', end='')
print()
for k, v in enumerate(times):
    print(f'{k:>2}  ', end='')
    for d in v.values():
        print(f'{str(d):<12}', end='')
    print()
print('-:' * 22)

while True:
    busca = int(input('Mostrar dados de qual jogador? (999 encerra.): '))
    if busca == 999:
        break
    if busca >= len(times):
        print(f'ERRO! Não existe jogador com código {busca}!')
    else:
        print(f' ---  LEVANTAMENTO DO JOGADOR - {times[busca]["nome"]}:')
        for i, g in enumerate(times[busca]['gols']):
            print(f'    No jogo {i+1} fez {g} gols.')
    print('-:' * 22)
print()
print(f'{' VOLTE SEMPRE! ':-^44}')

