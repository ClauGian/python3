
#import math
#num = int(input('Digite um número para ver sua raiz: '))
#raiz = math.sqrt(num)
#print('A raiz quadrada de {} é igual a {:.2f}'.format(num, raiz))

# OUTRA MANEIRA DE IMPORTAR.

from math import sqrt
num = int(input('Digite um número para ver sua raiz: '))
raiz = sqrt(num)
print('A raiz quadrada de {} é igual a {:.2f}'.format(num, raiz))