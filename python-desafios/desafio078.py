print('*-' * 30)
print(f'{'VALORES MAIORES E MENORES E SUAS POSIÇÕES':^60}')
print('*-' * 30)
vlr = list()
for c in range(0, 5):
    vlr.append(int(input(f'Digite um valor para a Posição {c}: ')))
    maior = max(vlr)
    menor = min(vlr)
print(f'O maior valor digitado foi o número {maior} e está na posição {vlr.index(maior)}.')
print(f'O menor valor digitado foi o número {menor} e está na posição {vlr.index(menor)}.')

