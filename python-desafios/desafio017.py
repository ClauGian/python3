import math
print('Temos um triângulo retângulo com as seguintes medidas:')
co = float(input('Digite a medida do cateto oposto em cm: '))
ca = float(input('Digite a medida do cateto adjavcente em cm: '))
hip = math.sqrt(co ** 2 + ca ** 2)
print('O valor da hipotenusa é: {} formatando = {:.2f} cm'.format(hip, hip))

""" a formula é c² = a² + b² onde c = hipotenusa, a = cateto oposto e b = cateto adjacente
ou pode usar a formula pronta math.hypot """

co = float(input('Digite a medida do cateto oposto em cm: '))
ca = float(input('Digite a medida do cateto adjavcente em cm: '))
hip = math.hypot(co, ca)
print('O valor da hipotenusa é: {} formatando = {:.2f} cm'.format(hip, hip))
