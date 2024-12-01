"""def soma(a, b):
    print(f'A = {a}  e  B = {b}')
    s = a + b
    print(f'A soma A + B = {s}')

soma(4,8)"""
def contador(*num):
    #for valor in num:
    #    print(f'{valor} ', end='')
    #print(' Fim')
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} números')

contador(2, 1, 7)
contador(8, 0)
contador(4, 6, 8, 7, 2, 9)

