print('{:=^40}'.format(' EXERCÍCIO SOBRE MATRIZ '))
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = scol = mai = 0
for l in range(0, 3):
    for c in range (0, 3):
        matriz[l][c] = int(input(f'    Digite um valor para [{l}, {c}]: '))

print('{:=^40}'.format(' M A T R I Z '))
for l in range(0, 3):
    for c in range(0, 3):
        print(f'   [{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]
    print()
print('=' * 40)
print(f'A soma dos valores pares da matriz é {spar}.')
for l in range(0, 3):
    scol += matriz[l][2]
print(f'A soma dos valores da 3ª coluna é: {scol}.')
for c in range(0, 3):
    if c == 0:
        mai = matriz[1][c]
    elif matriz[1][c] > mai:
        mai = matriz[1][c]
print(f'O maior valor da 2ª linha é: {mai}.')
print('{:=^40}'.format(' F I M '))
