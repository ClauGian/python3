valores = []
pares = []
impares = []
while True:
    valores.append(int(input('Digite um valor: ')))
    resp = str(input('Continuar? [S/N]: ')).upper().strip()[0]
    if resp == 'N':
        break

for p in valores:
    if p % 2 == 0:
        pares.append(p)
for i in valores:
    if i % 2 == 1:
        impares.append(i)
print('-*' * 25)
print(f'Os valores digitados foram: {valores}.')
print(f'Os valores PARES digitados foram: {pares}.')
print(f'Os valores IMPARES digitados foram: {impares}. ')




