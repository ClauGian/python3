import math
a = float(input('Informe um ângulo para calculo do seno, cosseno e tangente: '))
sen = math.sin(math.radians(a))
cos = math.cos(math.radians(a))
tan = math.tan(math.radians(a))
print('Em um ângulo de {}° '.format(a))
print('O valor do seno é: {:.2f}.'.format(sen))
print('O valor do cosseno é: {:.2f}.'.format(cos))
print('E o valor da tangente é: {:.2f}.'.format(tan))