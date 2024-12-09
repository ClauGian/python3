jogo = {}
gols = []
jogo['nome'] = str(input('Nome do Jogador: '))
qtde = int(input(f'Quantas partidas {jogo['nome']} jogou? '))
print('--' * 25)
for c in range(1, qtde + 1):
    gols.append(int(input(f'Quantos gols {jogo['nome']} fez na {c}ª partida? ')))
    totgols = sum(gols)
    jogo['gols'] = gols
    jogo['total'] = totgols
print('-+' * 25)
print(jogo)

print('-+' * 25)
print(f'O campo nome tem o valor: {jogo['nome']}.')
print(f'O campo gols tem o valor: {jogo['gols']}.')
print(f'O campo total tem o valor: {jogo['total']}.')
print('-+' * 25)
print(f'O jogador {jogo['nome']} jogou {qtde} partidas.')
for c in range(1, qtde + 1):
    print(f'    ==> Na partida {c}, fez {jogo['gols']} gols.')
print()
print(f'Foi um total de {jogo['total']} gols.')




