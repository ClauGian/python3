from datetime import datetime
ano = datetime.now().year
cadastro = {}
while True:
    cadastro['Nome'] = str(input('Nome: '))
    nasc = int(input('Ano de nascimento: '))
    cadastro['Idade'] = ano - nasc
    cadastro['CTPS'] = int(input('Carteira de trabalho (0 = não tem): '))
    if cadastro['CTPS'] == 0:
        break
        for k, v in cadastro.items():
            print(f'{k} tem o valor {v}.')
    cadastro['Contratação'] = int(input('Ano de contratação: '))
    cadastro['Salário'] = float(input('Salario R$: '))
    cadastro['Aposentadoria'] = (cadastro['Contratação'] + 35) - nasc
    break
print('-*' * 15)
for k, v in cadastro.items():
    print(f' → {k} tem o valor {v}.')
print('Fim...')