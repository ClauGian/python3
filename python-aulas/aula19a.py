print('Criando um dicionário dentro de uma lista.')

brasil = []
estado1 = {'uf': 'São Paulo', 'sigla': 'SP'}
estado2 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
brasil.append(estado1)
brasil.append(estado2)
print(estado1)
print(estado2)
print(brasil)
print(brasil[0])
print(brasil[1])
print(brasil[0]['uf'])
print(f'A cidade de {brasil[0]['uf']} é demais, e fica no estado de {brasil[0]['sigla']}.')
print()
estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do estado: '))
    brasil.append(estado.copy())
print(brasil)
print()
for e in brasil:
    print(e)
print()
for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}.')
print()
for e in brasil:
    for v in e.values():
        print(v, end=' - ')
    print()

