
resp = 's'
qtde = soma = media = maior = menor = 0
while resp in 'Ss':
    n = int(input('Digite um número: '))
    resp = str(input('Deseja continuar? [s / n]: ')).upper().strip()[0]
    qtde += 1
    soma += n
    media = soma / qtde
    if qtde == 1:
        maior = menor = n
    else:
        if n < menor:
            menor = n
        if n > maior:
            maior = n

print('Foram digitados {} números.'.format(qtde))
print('A soma dos números digitados foi: {}.'.format(soma))
print('A média entre os números digitados é: {:.1f}.'.format(media))
print('O maior valor digitado foi o {}.'.format(maior))
print('O menor valor digitado foi o {}.'.format(menor))

