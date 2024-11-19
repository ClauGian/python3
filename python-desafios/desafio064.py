# NÃO CONSEGUI.
n = ''
qtde = 0
s = 0
c = 1
while n != 999:
    n = int(input('Digite o {}º um número: '.format(c)))
    qtde = (c + 1) - 2
    s = (s + n)
    c = c + 1
print('{}'.format(qtde), end=' - ')
print('{}'.format(s), end=' - ')
