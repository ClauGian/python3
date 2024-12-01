merc = ('Veneziana', 680.00,
        'Tinta 18l', 560.00,
        'Tinta 3,6l', 187.00,
        'Cimento', 126.00,
        'Cal', 48.00,
        'Tubo 6mts', 80.00,
        'cotovelo 3/4', 3.50,
        'Pincel', 2.50,
        'Lixa', 1.20)

print('=:' * 23)
print(f'{"LISTAGEM DE PREÇO":^46}')
print('-:' * 23)
for p, v in enumerate(merc):
    if p % 2 == 0:
        print(f'   {merc[p]:.<30}', end='')

    else:
        print(f'R$ {merc[p]:>7.2f}')
print('-:' * 23)
