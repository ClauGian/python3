par = 0
num = (int(input('Digite um número: ')),
       int(input('Digite outro número: ')),
       int(input('Digite mais um número: ')),
       int(input('Digite o último número: ')))
print(f'Você digitou os valores: {num}')
print(f'O número 9 apareceu {num.count(9)} vezes.')
if 3 in num:
    print(f'O número 3 apareceu na {num.index(3)} posição.')
else:
    print('O número 3 não apareceu em nenhuma posição.')
print(f'Os valores pares digitados foram: ', end='')
for c in num:
    if c % 2 == 0:
        print(c, end=' ')
print()
