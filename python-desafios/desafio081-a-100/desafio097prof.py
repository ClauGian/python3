def escreva(msg):
    tam = len(msg) + 6
    print('~' * tam)
    print(f'{msg:^{tam}}')
    print('~' * tam)

#Programa principal
escreva('Clau Gian')
escreva('Vamos aprender Python rapidamente.')
escreva('Sim!')

