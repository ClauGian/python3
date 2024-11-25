palavras = []
vogais = ('a', 'e', 'i', 'o', 'u')

for c in range(1, 4):
    p = str(input('Digite uma palavra: ')).upper()
    palavras.append(p)
palavras = tuple(palavras)

for palavra in palavras:
    print(f'A palavra {palavra} possui as vogais: ')
    for letras in palavras:
        if letras in vogais:
            print(letras)
            break


