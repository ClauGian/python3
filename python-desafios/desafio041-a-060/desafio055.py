maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input('Informe o peso da {}ª pessoa: '.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print()
print('O menor peso lido foi de {}Kg.'.format(menor))
print('O maior peso lido foi de {}Kg.'.format(maior))

