s = 0
for n in range(1, 7):
    i = int(input('Digite um número: '))
    if i % 2 == 0:
        s = s + i
print('A soma dos números pares digitados é ({}).'.format(s))