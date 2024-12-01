jogo = {}
jogolist = []
gols = []
totgols = 0
while True:
    nome = str(input('Nome do Jogador: '))
    qtde = int(input(f'Quantas partidas {nome} jogou? '))
    print('--' * 25)
    for c in range(1, qtde + 1):
        gols = int(input(f'Quantos gols {nome} fez na {c}ª partida? '))
    totgols += gols
    resp = str(input('Deseja continuar? [S/N]: ')).upper(). strip()[0]
    if resp == 'N':
        break
print('-+' * 25)
jogolist.append([nome, gols, totgols])
print(jogolist)
print(f'{"Cod":<5} {"Nome":<8} {"Gols":>8} {"Total":>8}')
for i, a in enumerate(jogolist):
    print(f' {i:<5}{a[0]:<8}{ a[1]:>9.1f}{a[2]:>9.1f}')
while True:
    print()
    opção = int(input('Mostrar notas de qual aluno? '
                      '[999 para interromper.]: '))
    if opção == 999:
        print('>>>> FINALIZANDO...')
        break

print('-+' * 25)
print(f'O jogador {jogo['nome']} jogou {qtde} partidas.')
for c in range(1, qtde + 1):
    print(f'    ==> Na partida {c}, fez {jogo['gols']} gols.')
print()
print(f'Foi um total de {jogo['total']} gols.')



