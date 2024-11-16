a = float(input('Informe a medida do lado A: '))
b = float(input('Informe a medida do lado B: '))
c = float(input('Informe a medida do lado C: '))
if a < b + c and b < a + c and c < a + b:
    print(' As medidas {}, {} e {} FORMAM um triângulo.'.format(a, b, c))
else:
    print(' As medidas {}, {} e {} NÃO FORMAM um triângulo.'.format(a, b, c))
