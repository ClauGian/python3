#comando help()
#Para saber mais sobre um determinado comando é só usar o help assim:
#help(print)
#O conteudo é impresso na execução
#help(enumerate)
def contador(i, f, p):
    """
     - Faz uma contagem e mostra na tela
    :param i: inicio da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: não tem retorno
    """
    c = i
    while c <= f:
        print(f'{c}', end='')
        c += p
    print(' Fim')

#help(contador) Vai mostrar o que está acima
"""
def somar(a=0, b=0, c=0):
    s = a + b + c
    return s

r1 = somar(3, 5, 7)
r2 = somar(6, 4)
r3 = somar(9)
print(f'A soma dos valores foram: {r1}, {r2} e {r3}')"""

"""def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f

#n = int(input('Digite um número: '))
#print(f'O fatorial de {n} é igual a {fatorial(n)}')

f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resultados são: {f1}, {f2} e {f3}.') """

def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False

num = int(input('Digite um valor: '))
if par(num):
    print('É par')
else:
    print('É Impar')


