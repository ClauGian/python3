import sys
resp = 's'
qtde = 0
soma = 0
media = 0
maior = 0
menor = sys.maxsize
c = 1
while c == (resp == 's'):
    n = int(input('Digite um número: '))
    resp = str(input('Deseja continuar? [s / n]: '))
    qtde = qtde + 1
    soma = soma + n
    media = soma / qtde
    if n == 1:
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

