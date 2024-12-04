from random import randint

num = []
mai = men = par = impar = soma = 0
for c in range(0, 5):
    n = randint(0, 9)
    num.append(n)
mai = max(num)
men = min(num)
soma = sum(num)
print(f'Os números apresentados são: {num}')
print('Dentre os apresentados, temos os números PARES: ', end='')
for c in num:
    if c % 2 == 0:
        print(f'[{c}]..', end=' ')
print()
print('Dentre os apresentados, temos os números ÍMPARES: ', end='')
for c in num:
    if c % 2 == 1:
        print(f'[{c}]..', end=' ')
print()
print(f'Dentre os apresentados, temos o número MAIOR: [ {mai} ]')
print(f'Dentre os apresentados, temos o número MENOR: [ {men} ] ')
print(f'E por fim, a soma de todos os números apresentados é: [ {soma} ]')

