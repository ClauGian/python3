print('=' * 40)
print('{:^40}'.format(' B A N C O   C & G '))
print('=' * 40)
valor = int(input('    Qual valor vai sacar? R$ '))
print('{:^40}'.format('.................'))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'    Total de {totced} cédulas de R$ {ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 5
        elif ced == 5:
            ced = 1
        totced = 0
        if total == 0:
            break
print('=' * 40)
print('{:^40}'.format(' B A N C O   C & G '))
print('=' * 40)
print('{:^40}'.format('Volte Sempre. Tenha um bom dia.'))
print('.' * 40)