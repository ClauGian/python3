qtde = soma = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    qtde += 1
    soma += n
print(f'Foram digitados {qtde} números, que somados atingiram o valor de: {soma}.')

