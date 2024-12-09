turma = list()

while True:
    aluno = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    média = (nota1 + nota2) / 2
    turma.append([aluno, [nota1, nota2], média])
    resp = str(input('Deseja Continuar? [S/N]: ')).upper().strip()[0]
    if resp == 'N':
        break
print('-*' * 30)
print(f' {"Nº.":<5}{"NOME":<10}{"MÉDIA":>8}')
print('--' * 30)
for i, a in enumerate(turma):
    print(f' {i:<5}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print()
    opção = int(input('Mostrar notas de qual aluno? '
                      '[999 para interromper.]: '))
    if opção == 999:
        print('>>>> FINALIZANDO...')
        break
    print(f'As notas de {turma[opção][0]} são {turma[opção][1]}')
print('-.' * 30)
print('{:-^60}'.format('<< VOLTE SEMPRE >>'))

