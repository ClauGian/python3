from time import sleep
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))

r = 0
c = 1
maior = 0
opção = 0
while opção != 5:
    print('''O que deseja fazer?
[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos números
[ 5 ] Sair''')
    opção = int(input('Qual a sua opção? '))
    print()
    if opção == 1:
        r = n1 + n2
        print('A soma entre {} e {} é igual a: {}.'.format(n1, n2, r))
        print()
    if opção == 2:
        r = n1 * n2
        print('A multiplicação entre {} e {} é igual a: {}.'.format(n1, n2, r))
        print()
    if opção == 3:
        if n1 > maior:
            maior = n1
        if n2 > maior:
            maior = n2
        print('O maior número entre {} e {} é o número: {}.'.format(n1, n2, maior))
        print()
    if opção == 4:
        print('Informe os novos valores:')
        n1 = int(input('Digite o novo valor: '))
        n2 = int(input('Digite o novo valor: '))
        print()
    if opção < 1 or opção > 5:
        print('Você digitou ERRADO! Tente novamente.')
        print()
    print('=-=' * 20)
    sleep(2)
print('Fim do programa. Volte sempre.')

