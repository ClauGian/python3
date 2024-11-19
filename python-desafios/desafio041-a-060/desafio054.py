from datetime import date
anoa = date.today().year
maior = 0
menor = 0

for c in range(1, 8):
    nasc = int(input('Em que ano a {}ª pessoa nasceu? '.format(c)))
    idade = anoa - nasc
    if idade <= 21:
        menor = menor + 1
    if idade > 21:
        maior = maior + 1
print('Tivemos {} pessoas menores de idade.'.format(menor))
print('Tivemos {} pessoas maiores de idade.'.format(maior))

