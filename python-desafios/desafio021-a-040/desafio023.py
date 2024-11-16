num = int(input('Escreva um número entre 0 e 9999: '))
uni = num // 1 % 10
dez = num // 10 % 10
cen = num // 100 % 10
mil = num // 1000 % 10
print('Você digitou o número: {}'.format(num))
print('A sua unidade é: {}'.format(uni))
print('A sua dezena  é: {}'.format(dez))
print('A sua centena é: {}'.format(cen))
print('A sua milhar  é: {}'.format(mil))


