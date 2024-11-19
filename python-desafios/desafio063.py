n = int(input('Digite um Número: '))
c = 0
t1 = 0
print(t1, end=' - ')
t2 = 1
print(t2, end=' - ')
while c < n:
    t3 = t1 + t2
    print(t3, end=' - ')
    t1 = t2
    t2 = t3
    c = c + 1