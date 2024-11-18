maior = 0
menor = 0

for n in range(0, 5):
    nome = str(input('Qual seu nome? '))
    peso = float(input('Qual seu peso: '))
    if peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso
print('Quem teve o menor peso foi {}, com {}kg'.format(nome, menor))
print('Quem teve o maior peso foi {}, com {}kg'.format(nome, maior))

