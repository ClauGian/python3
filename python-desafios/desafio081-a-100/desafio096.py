def área(larg, comp):
    dime = larg * comp
    print(f'A área do terreno com medidas {larg} x {comp} correspende a {dime} m².')

#Programa principal
print('-:' * 20)
print(f'{"CONTROLE DE TERRENOS":^40}')
print('--' * 20)
l = float(input('Qual a largura do terreno em (mts): '))
c = float(input('Qual o comprimento do terreno em (mts): '))
área(l, c)