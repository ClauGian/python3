s = 0
q = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        q = q + 1
        s += c
print('Temos {} números impares divisíveis por 3 entre 1 e 500, que somam {}.'.format(q, s))

