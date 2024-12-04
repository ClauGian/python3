valores = []
while True:
    num = int(input('Digite um valor: '))
    if num not in valores:
        valores.append(num)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não será adicionado.')
    resp = str(input('Deseja Continuar? [S/N]: ')).upper().strip()[0]
    if resp == 'N':
        break
print('-*' * 20)
valores.sort()
print(f'Você digitou os valores: {valores}')

