matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
par = soma = mai = 0
for lin in range(0, 3):
    for col in range(0, 3):
        matriz[lin][col] = int(input(f'Digite um valor para posição {lin}, {col}: '))

        if matriz[lin][col] % 2 == 0:
            par += matriz[lin][col]
for lin in range(0, 3):
    for col in range(0, 3):
        print(f'    [{matriz[lin][col]:^5}]', end=' ')
    print()
print(f'A soma dos valores pares é : {par}')
for lin in range(0, 3):
    soma += matriz[lin][2]
print(f'A soma dos valores da terceira coluna é: {soma}')
for col in range(0, 3):
    if col == 0:
        mai = matriz[1][col]
    elif matriz[1][col] > mai:
        mai = matriz[1][col]
print(f'O maior valor da segunda linha é: {mai}')


