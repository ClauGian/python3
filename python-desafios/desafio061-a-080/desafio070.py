
print('<->' * 12)
print('{:^44}'.format('\033[34m L O J A S   C & G \033[m'))
print('<->' * 12)
total = totmil = menor = cont = 0
barato = ''
while True:
    produto = str(input('Qual nome do produto? '))
    valor = float(input('Qual foi o preço? R$ '))
    cont += 1
    total += valor
    if valor > 1000:
        totmil += 1
    if cont == 1 or valor < menor:
        menor = valor
        barato = produto

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Continuar [S/N]: ')).upper().strip()[0]
    if resp == 'N':
        break

    print('...' * 12)
print(f'O total de compras foi de: {total:.2f}')
print(f'Temos {totmil} produtos com valor acima de R$ 1.000,00.')
print(f'O produto mais barato foi {barato} que custa R$ {menor:.2f}')