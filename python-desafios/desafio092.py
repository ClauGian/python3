from datetime import date

cadapos = {}
for c in range(0, 1):
    atual = date.today().year
    cadapos['nome'] = str(input('Nome: '))
    nasc = int(input('Ano de Nascimento: '))
    cadapos['nasc'] = nasc
    carteira = int(input('Carteira de trabalho (0 = não tem) nº: '))
    cadapos['ctps'] = carteira
    idade = atual - nasc
    cadapos['idade'] = idade
    if carteira == 0:
        print(f'Nome cadastrado: {cadapos['nome']}')
        print(f'Idade cadastrada: {cadapos['idade']}')
        print(f'CTPS cadastrada: {cadapos['ctps']}')
        break
    anoc = int(input('Ano de contratação: '))
    aposent = (anoc + 35) - nasc
    cadapos['contrat'] = anoc
    cadapos['salario'] = float(input('Salário: '))
    cadapos['idadeapos'] = aposent

    print('\033[34m*.\033[m' * 20)
    print(f'Nome cadastrado: {cadapos['nome']}')
    print(f'Idade cadastrada: {cadapos['idade']}')
    print(f'CTPS cadastrada: {cadapos['ctps']}')
    print(f'Ano da contratação: {cadapos['contrat']}')
    print(f'Valor do salário: {cadapos['salario']:.2f}')
    print(f'Idade para aposentadoria: {cadapos['idadeapos']}')



