números = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete',
           'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze',
           'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    n = int(input('Digite um números entre 0 e 20: '))
    if n < 0 or n > 20:
        print('Erro. Tente novamente => ', end='')
    else:
        print(f'O número que você digitou foi => "{números[n]}"')
        resp = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
        if resp == 'N':
            break

