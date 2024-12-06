cad = {}
pessoas = []
media = soma = 0
while True:
    cad.clear()
    cad['nome'] = str(input('Nome: '))
    while True:
        cad['sexo'] = str(input('Sexo [M/F]: ')).upper().strip()[0]
        if cad['sexo'] in 'MF':
            break
        print('Erro! Digite "M" ou "F".')
    cad['idade'] = int(input('Idade: '))
    soma += cad['idade']
    pessoas.append(cad.copy())

    while True:
        resp = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
        if resp in 'SN':
            break
        print('A resposta deve ser "S" ou "N".')
    if resp == 'N':
        break

print(f'A) Foram cadastradas {len(pessoas)} pessoas.')
media = soma / len(pessoas)
print(f'B) A média de idade é de {media:.1f} anos.')
print('C) As mulheres cadastradas foram: ', end='')
for p in pessoas:
    if p['sexo'] == 'F':
        print(f'{p['nome']:→>}', end='  ')
print()
print('D) Lista das pessoas que estão acima da média de idade:')
print()
for p in pessoas:
    if p['idade'] >= media:
        for k, v in p.items():
            print(f'   > {k} = {v}   ', end='')
print()