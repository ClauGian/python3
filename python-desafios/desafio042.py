a = float(input('Qual a medida do lado A: '))
b = float(input('Qual a medida do lado B: '))
c = float(input('Qual a medida do lado C: '))
tr = (a <= (b + c)), (b <= (a + c)), (c <= (a + b))
eq = [(a == b), (a == c), (b == c)]
iso = [(a == b != c), (a == c != b), (b == c != a) ]
esc = [(a != b), (a != c), (b != c)]
if (a == b) and (a == c) and (b == c):
    print('Com as medidas {}, {} e {} formam um triângulo \033[34mEQUILÁTERO\033[m.'.format(a, b, c))
elif a < b + c and b < a + c and c < a + b and a == b or a == c or b == c:
    print('Com as medidas {}, {} e {} formam um triângulo \033[34mISÓSCELES\033[m.'.format(a, b, c))
elif (a < (b + c)) and (b < (a + c)) and (c < (a + b)) and (a != b) and (a != c) and (b != c):
    print('Com as medidas {}, {} e {} formam um triângulo \033[34mESCALENO\033[m.'.format(a, b, c))
else:
    print('Com as medidas {}, {} e {}, \033[34mNÃO SE FORMA UM TRIÂNGULO\033[m.'.format(a, b, c))
