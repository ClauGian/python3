pessoa = dict()
galera = list()
soma = media = 0
print()
print(f'{"> C  A  D  A  S  T  R  O <":=^60}')
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo [M/F]: ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor digite somente "M" ou "F".')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())

    while True:
        resp = str(input('Deseja continuar? [S/N]: ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! A resposta deve ser "S" ou "N".')
    if resp == 'N':
        break
print('=.' * 30)
print(f' A) Ao todo foram cadastradas {len(galera)} pessoas.')
print('---')
media = soma / len(galera)
print(f' B) A média das idades é de: {media:.2f} anos.')
print('---')
print(' C) As mulheres cadastradas foram: ',end='')

for p in galera:
    if p['sexo'] == 'F':
        print(f'{p['nome']} ', end=' ')
print()
print('---')
print(' D) Lista das pessoas que estão acima da média de idade:')
for p in galera:
    if p['idade'] >= media:
        print('     ')
        for k, v in p.items():
            print(f'  - {k} = {v}, ', end='')
        print()
print()
print(f'{  "ENCERRADO"   :=^60}')

