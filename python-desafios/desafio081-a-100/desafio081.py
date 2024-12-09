n = list()
qtde = 0
resp = 'S'
while resp != 'N':
    n.append(int(input('Digite um número: ')))
    resp = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
    qtde += 1 # pode usar len(n)
print('*-' * 30)
print(f'Você digitou {qtde} valores que foram: {n}.')
n.sort(reverse=True)
print(f'Os valores em ordem decrescente ficam assim: {n}.')
if 5 in n:
    print(f'O número "5" esta na posição decrescente nº {n.index(5)}.')
else:
    print('O número "5" não está na lista.')
print('*-' * 30)
