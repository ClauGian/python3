dados = []
mai = men = 0
cad = []
while True:
    dados.append(str(input('Qual seu nome: ')))
    dados.append(float(input('Qual seu peso: ')))
    if len(cad) == 0:
        mai = men = dados[1]
    else:
        if dados[1] > mai:
            mai = dados[1]
        if dados[1] < men:
            men = dados[1]
    cad.append(dados[:])
    dados.clear()
    resp = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
    if resp == 'N':
        break
print(cad)

print(f'Ao todo foram cadastradas {len(cad)} pessoas.')
print(f'O maior peso foi de {mai} kg. Peso de ', end='')
for p in cad:
    if p[1] == mai:
        print(f'[{p[0]}]', end=' ')
print()
print(f'O menor peso foi de {men} kg. Peso de ',end='')
for p in cad:
    if p[1] == men:
        print(f'[{p[0]}]', end=' ')
print()



