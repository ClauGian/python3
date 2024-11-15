dist = int(input('Qual a distância de sua viagem em km:? '))
if dist <= 200:
    preco = dist * 0.50
    print('O preço de sua passagem é de: R$ {:.2f}'.format(preco))
else:
    preco = dist * 0.45
    print('O preço de sua passagem é de: R$ {:.2f}'.format(preco))

