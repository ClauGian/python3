

listagem = ('Tinta 18l', '527.00',
            'Tinta 3,6l', '196.50',
            'Veneziana 2x1', '796',
            'Porta Sanfonada', '272.40',
            'Tubo PVC 6"', '110',
            'Tubo PVC 3/4', '42.65',
            'Cimento', '198.5',
            'Cal', '64',
            'Rejunte', '27.50',
            'Broca', '13.80')

print('.=' * 20)
print(f'{'LISTAGEM DE PREÇOS':^40}')
print('.=' * 20)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print('R$ {:>7.2f}'.format(float(listagem[pos])))
print('.=' * 20)


