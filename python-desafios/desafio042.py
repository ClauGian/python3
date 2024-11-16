a = float(input('Qual a medida do lado A: '))
b = float(input('Qual a medida do lado B: '))
c = float(input('Qual a medida do lado C: '))

if a == b and b == c:
    print('Com as medidas {}, {} e {} formam um triângulo \033[34mEQUILÁTERO\033[m.'.format(a, b, c))

elif a == b or b == c or c == a and (b <= (a + c) and a < (b + c) and c < (a + b)):
    print('Com as medidas {}, {} e {} formam um triângulo \033[34mISÓSCELES\033[m.'.format(a, b, c))

elif a != b and a != c and b != c and (a < (b + c) and b < (a + c) and c < (a + b)):
    print('Com as medidas {}, {} e {} formam um triângulo \033[34mESCALENO\033[m.'.format(a, b, c))

else:
    print('Com as medidas {}, {} e {}, \033[34mNÃO SE FORMA UM TRIÂNGULO\033[m.'.format(a, b, c))
