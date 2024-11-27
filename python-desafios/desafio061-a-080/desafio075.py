
n = (int(input('Digite um número: ')), int(input('Digite outro número: ')), int(input('Digite mais um número: ')), int(input('Digite o último número: ')))
print('..' * 15)
print(f'Você digitou os números: {n}.')
print('..' * 5)
print(f'O valor 9 apareceu {n.count(9)} vezes.')
print('..' * 5)
if 3 not in n:
    print('O número 3 não foi digitado.')
else:
    print(f'O valor 3 apareceu na {(n.index(3))+1}ª posição.')
print('..' * 5)
print('Os valores pares digitados foram: ', end='')
for num in n:
    if num % 2 == 0:
        print(num, end=' ')
print()
print('..' * 15)


