import sys
print('<->' * 12)
print('{:^44}'.format('\033[34m L O J A S   C & G \033[m'))
print('<->' * 12)
resp = nome = ''
preço = total = caro = menor = 0

while resp != 'N':
    nome = str(input('Nome produto: '))
    preço = int(input('Qual o preço: '))

    total += preço
    if preço >= 1000:
        caro += 1
    if nome == 1:
        menor = preço
    else:
        if preço < menor:
            menor = preço


    resp = str(input('Continuar [S/N]: ')).upper()
    print('...' * 12)
print(f'O total de compras foi de: {total:.2f}')
print(f'Temos {caro} produtos com valor acima de R$ 1.000,00.')
print(f'O produto mais barato foi {nome} no valor de R$ {menor}')