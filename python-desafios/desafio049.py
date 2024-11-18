
n = int(input('Você quer ver a TABUADA de que número? '))
print('\033[4;30;42m== T A B U A D A  ==\033[m')
for i in range(0, 11):
    print('|\033[32m{:-2d}\033[m  X  \033[31m{:-2d}\033[m  =  \033[34m{:-3d}\033[m |'.format(n, i, (n * i)))
print('\033[30;42m=\033[m' * 20)

