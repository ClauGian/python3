palavras = ()
vog = 'aeiou'
letras = ()
pal = []
for c in range(1, 7):
    palavras = (str(input('Digite uma palavra: ')))
    pal.append(palavras)
print()
print(':-' * 30)
print(f'{" APRESENTANDO VOGAIS ":^60}')
print(':-' * 30)
for n in pal:
    print(f'{f'A palavra {n.upper()} possui as vogais:':.<45} ', end='')
    for letras in n:
        if letras in vog:
            print(f'{letras:>1}', end=' ')
    print()
print(':-' * 30)

