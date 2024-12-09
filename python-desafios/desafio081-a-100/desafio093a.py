aprov = {}
gols = []
tot = 0
aprov['nome'] = str(input('Nome do Jogador: '))
qt = int(input(f'Quantas partidas {aprov['nome']} jogou? '))
for p in range(1, qt+1):
    gols.append(int(input(f'Quantos gols marcados na {p}ª partida: ')))

aprov['gols'] = gols.copy()
aprov['tot_gols'] = sum(gols)
print('-:' * 20)
print(aprov)
print('-:' * 20)
for k, v in aprov.items():
    print(f'O campo {k} tem o valor {v}.')
print('-:' * 20)
print(f'O jogador {aprov["nome"]} jogou {qt} partidas:')
for p, g in enumerate(gols):
    print(f'  ==> Na {p+1}ª partida, fez {g} gols.')
print(f' → {aprov["nome"]} marcou um total de {aprov["tot_gols"]} gols')
