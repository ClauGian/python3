c = 0
while True:
    n = int(input('Quer ver a tabuada de que número? '))
    print('-.' * 20)
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n}  x  {c}  =  {n * c}')
    print('-.' * 20)
print('PROGRAMA TABUADA ENCERRADO! Volte Sempre!')

