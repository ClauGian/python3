from datetime import date
anoa = date.today().year
maior = 0
menor = 0
for c in range(0, 7):
    nasc = int(input('Em que ano nasceu? '))
    idade = anoa - nasc
    if idade <= 21:
        menor = menor + 1
    elif idade > 21:
        maior = maior + 1
print('Tivemos {} pessoas que não atingiram a maioridade:'.format(menor))
print('Tivemos {} pessoas que atingiram a maioridade:'.format(maior))

