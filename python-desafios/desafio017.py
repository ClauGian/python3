import math
print('Temos um triângulo retângulo com o cateto oposto medindo 4cm \ne o cateto adjacente medindo 7cm. Calcular a hipotenusa.')
co = 4
ca = 7
hip = math.sqrt(co ** 2 + ca ** 2)
print('O valor da hipotenusa é: {} ou {:.2f}cm'.format(hip, hip))

# a formula é c² = a² + b² onde c = hipotenusa, a = cateto oposto e b = cateto adjacente