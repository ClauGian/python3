from random import randint
v = 0
while True:
    jogador = int(input('Qual seu número? '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PpIi':
        tipo = str(input('Quer Par ou Impar?[P / I]: ')).strip().upper()[0]
    print(f'Você jogou {jogador} e computador jogou {computador}.')
    print(f'O total foi: {total}  → →  DEU PAR' if total % 2 == 0 else 'DEU IMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você venceu!!!')
            v += 1
        else:
            print('Você perdeu!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você venceu!!!')
            v += 1
        else:
            print('Você perdeu!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER!! Você venceu {v} vezes.')




