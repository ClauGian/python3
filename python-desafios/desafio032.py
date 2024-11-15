ano = int(input('Digite um ano qualquer: '))
if ano % 4 == 0 and ano % 400 == 0:
    print('O ano de {}, é BISSEXTO.'.format(ano))
else:
    print('O ano de {}, não é bissexto.'.format(ano))

