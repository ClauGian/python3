soma = 0
qtde = 0
for n in range(1, 7):
    i = int(input('Digite um número: '))
    if i % 2 == 0:
        soma += i
        qtde += 1
print('A soma dos {} números pares digitados é ({}).'.format(qtde, soma))