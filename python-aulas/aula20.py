"""def soma(a, b):
    print(f'A = {a}  e  B = {b}')
    s = a + b
    print(f'A soma A + B = {s}')
soma(4,8)"""


"""def contador(*num):
    #for valor in num:
    #    print(f'{valor} ', end='')
    #print(' Fim')
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} números')
contador(2, 1, 7)
contador(8, 0)
contador(4, 6, 8, 7, 2, 9)"""

"""
def dobra(lista):
    pos = 0
    while pos < len(valores):
        lista[pos] *= 2
        pos += 1
valores = [8, 15, 27, 12, 9, 32]   # Essa é a lista
print(valores)
dobra(valores)
print(valores)"""

def soma(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}.')
soma(7, 5)
soma(13, 9, 27)


