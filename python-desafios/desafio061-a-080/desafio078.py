print('*-' * 30)
print(f'{'VALORES MAIORES E MENORES E SUAS POSIÇÕES':^60}')
print('*-' * 30)
vlr = list()
for c in range(0, 5):
    vlr.append(int(input(f'Digite um valor para a Posição {c}: ')))
    maior = max(vlr)
    menor = min(vlr)
print(f'Você digitou os seguintes valores: {vlr}')
print(f'O maior valor digitado foi o número {maior} e está nas posições: ', end='')
for i, v in enumerate(vlr):
    if v == maior:
        print(f'{i}...', end='')
print()
print(f'O menor valor digitado foi o número {menor} e está nas posições: ', end='')
for i, v in enumerate(vlr):
    if v == menor:
        print(f'{i}...', end='')
print()

