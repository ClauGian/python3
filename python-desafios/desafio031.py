dist = float(input('Qual a distância de sua viagem? '))
print('Você está prestes a iniciar uma viagem de {} Km'.format(dist))
if dist <= 200:
    preco = dist * 0.50
else:
    preco = dist * 0.45
print('O preço de sua passagem é de: R$ {:.2f}'.format(preco))
print('Faça uma boa viagem!')

