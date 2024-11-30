cadastro = {}
cad = []
soma = 0
media = 0
qtde = 0
mulheres = ' '
acima = ''
while True:
    nome = str(input('Nome: '))
    cadastro['nome'] = nome
    idade = float(input('Idade: '))
    soma += idade
    cadastro['idade'] = idade
    sexo = str(input('Sexo [M/F]: ')).upper().strip()[0]
    cadastro['sexo'] = sexo
    resp = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
    qtde += 1
    media = soma / qtde
    cadastro['media'] = media
    if sexo == 'F':
        mulheres += nome
    if ['idade'] > ['media']:
        acima = cadastro.items()
    cad.append(cadastro.copy())
    if resp == 'N':
        break
print(f' - O grupo possui {qtde} pessoas.')
print(f' - A média de idade é de {media} anos.')
print(f' - As mulheres cadastradas foram: {mulheres}.')
print(' - Lista das pessoas que estão acima da média:')
print(acima, end='')




