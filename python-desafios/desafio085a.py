num = []
par = []
impar = []
p = i = 0
for c in range(1, 8):
    n = int(input(f'Digite o {c} valor: '))
    if c % 2 == 0:
        p += c
        par.append(p)
    else:
        i += c
        impar.append(i)
    num.append(n)
print(f'Os valores pares digitados foram: {par}')
print(f'Os valores impares digitados foram {impar}')