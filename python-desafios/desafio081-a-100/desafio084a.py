geral = list()
dados = list()
mai = men = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    if len(geral) == 0:
        mai = men = dados[1]
    else:
        if dados[1] > mai:
            mai = dados[1]
        if dados[1] < men:
            men = dados[1]
    geral.append(dados[:])
    dados.clear()
    resp = str(input('Continua? [S/N]: ')).upper().strip()[0]
    if resp == 'N':
        break
print(f'Foram cadastradas {len(geral)} pessoas.')
print(f'O maior peso foi {mai} kg de: ', end='')
for p in geral:
    if p[1] == mai:
        print(f'{p[0]}', end=' ')
print()
print(f'O menor peso foi {men} kg de: ', end='')
for p in geral:
    if p[1] == men:
        print(f'{p[0]}', end=' ')
print()


