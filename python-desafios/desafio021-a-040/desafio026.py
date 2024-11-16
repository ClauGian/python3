import unicodedata
frase = str(input(r'Digite uma frase qualquer: ')).lower()
frase2 = ''.join(ch for ch in unicodedata.normalize('NFKD', frase)
    if not unicodedata.combining(ch))
qtde = frase2.count('a')
prim = frase2.strip().find('a')
ulti = frase2.strip().rfind('a')

print('A frase acima possui {} letras (a).'.format(qtde))
print('A primeira letra (a) esta na posição {}'.format(prim))
print('A última letra (a) está na posição {}'.format(ulti))


