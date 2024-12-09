print('<->' * 15)
print(f'{"CADASTRO DE TURMA":^45}')
print('<->' * 15)
turma = []
notas = []
media = 0
while True:
    nome = str(input('Nome: '))
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    media = (n1 + n2) / 2
    turma.append([nome, [n1, n2], media])
    resp = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
    print('-:-' * 15)
    if resp == 'N':
        break

print(f'{"cod":<6}{"Nome":<10}{"Média":>10}')
for c, v in enumerate(turma):
    print(f' {c:<5}{v[0]:<10}{v[2]:>9}')
print('-:-' * 15)
while True:
    resumo = int(input('Mostrar notas de qual aluno? (999-Parar): '))
    for c, v in enumerate(turma):
        if resumo == c:
            print(f'As notas de {v[0]} são {v[1]}.')
    print('-:-' * 15)
    if resumo == 999:
        break
print('Finalizando...')
print('{:-^45}'.format('Volte Sempre'))




