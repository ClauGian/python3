val = []

while True:
    val.append(int(input('Digite um valor: ')))
    resp = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
    if resp == 'N':
        break
print('-*' * 30)
print(f'Foram digitados {len(val)} elementos.')
# Pode-se usar o → val.sort(reverse=True) → antes da resposta e manda imprimir o → val.
print(f'Os valores em ordem decrescente são: {sorted(val, key=int, reverse=True)}')
if 5 in val:
    print(f'O número 5 encontra-se na lista na posição {val.index(5)}.')
else:
    print('O número 5 não foi encontrado na lista.')



