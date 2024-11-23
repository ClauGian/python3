nome = 'José'
idade = 55
salario = 1412.00
print(f'{nome} tem {idade} anos e ganha R$ {salario:.2f}.')

n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
print(f'A soma dos valores é {s}.')