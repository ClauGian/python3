números = list()
while True:
    n = int(input('Digite um número: '))
    if n not in números:
        números.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Número duplicado! Não será adicionado.')
    resp = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
    if resp in 'N':
        break
print('*-' * 20)
números.sort()
print(f'Você digitou os números {números}.')
print('*-' * 20)

