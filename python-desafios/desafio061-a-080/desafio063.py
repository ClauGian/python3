print('*-*' * 12)
print('     Sequência de Fibonacci')
print('*-*' * 12)
n = int(input('Quantos termos deseja exibir: '))
print('¨¨' * 18)
c = 0
t1 = 0
print(t1, end=' → ')
t2 = 1
print(t2, end=' → ')
c = 3
while c <= n:
    t3 = t1 + t2
    print(t3, end=' → ')
    t1 = t2
    t2 = t3
    c = c + 1
print(' FIM')
print('¨¨' * 18)
