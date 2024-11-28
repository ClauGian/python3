pessoas = {'nome': 'Claudinei', 'sexo': 'M', 'idade': 55}
print(pessoas)
print(pessoas['nome'])
print(pessoas['idade'])
print(f'O {pessoas['nome']} tem {pessoas['idade']} anos.')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
for k in pessoas.keys():
    print(k)
for k in pessoas.values():
    print(k)
for k, v in pessoas.items():
    print(f'{k} = {v}')
print()
#del pessoas['sexo']  Excluiu o item sexo
pessoas['nome'] = 'Gianini'
for k, v in pessoas.items():
    print(f'{k} = {v}')
print()
pessoas['peso'] = 78
for k, v in pessoas.items():
    print(f'{k} = {v}')