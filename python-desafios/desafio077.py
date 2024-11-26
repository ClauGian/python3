palavras = []
vogais = ('a', 'e', 'i', 'o', 'u')
letras = []
for c in range(1, 7):
    p = str(input('Digite uma palavra: '))
    palavras.append(p)
palavras = tuple(palavras)

for n in palavras:
    print(f'\nA palavra {n.upper()} possui as vogais: ', end='')
    for letras in n:
        if letras.lower() in 'aeiou':
            print(letras, end=' - ')



