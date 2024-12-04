num = []
mai = men = 0
for c in range(0, 5):
    num.append(int(input(f'Digite o {c}º valor: ')))
mai = max(num)
men = min(num)
print(f'A lista contém os seguintes valores: {num}.')
print(f'O maior valor na lista é {mai} e suas posições são: ', end='')
for c, v in enumerate(num):
    if v == mai:
        print(f'{c}..', end=' ')
print()
print(f'O menor valor na lista é {men} e suas posições são: ', end='')
for c, v in enumerate(num):
    if v == men:
        print(f'{c}..', end='')
print()


