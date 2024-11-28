números = [[], []]

for c in range(1, 8):
    vlr = int(input(f'Digite o {c}º valor: '))
    if vlr % 2 == 0:
        números[0].append(vlr)
    else:
        números[1].append(vlr)
print('-*' * 25)

números[0].sort()
print(f'Os valores pares são: {números[0]}')
números[1].sort()
print(f'Os valores impares são: {números[1]}')
print('-*' * 25)

