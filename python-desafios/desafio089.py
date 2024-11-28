alunos= []
notas = []
média = []
print()
print(f'{"CADASTRO DE ALUNOS":=^50}')
while True:
    alunos.append(str(input('Nome: ')))
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    notas.append([n1] + [n2])
    resp = str(input('Deseja continuar?[S/N]: ')).upper().strip()[0]
    if resp == 'N':
        break
    print('-=' * 50)
    m = (n1 + n2) / 2
    média.append(m)




while True:
    c = int(input('Mostrar as notas de qual aluno? [999 interrompe]: '))
    if c == 999:
        break
    print(f'As notas de {alunos[c]} são {notas[c]} ')



