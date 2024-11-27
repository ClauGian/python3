valores = list()
par = []
impar = []

for c in range(0, 10):
    valores.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar: [S/N]: ')).upper().strip()[0]
    if resp in 'N':
        break
for p in valores:
    if p % 2 == 0:
        par.append(p)

for i in valores:
    if i % 2 == 1:
        impar.append(i)
print('*-' * 30)
print(f'Os valores digitados foram: {valores}.')
print(f'Dentre os valores acima, temos: {par} que são PARES.')
print(f'E também temos os valores {impar} que são IMPARES.')
print('*-' * 30)
