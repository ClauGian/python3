from random import shuffle
a1 = input('Digite o nome do aluno 1: ')
a2 = input('Digite o nome do aluno 2: ')
a3 = input('Digite o nome do aluno 3: ')
a4 = input('Digite o nome do aluno 4: ')
turma = [a1, a2, a3, a4]
shuffle(turma)
print('Os alunos são: {}, {}, {} e {}'.format(a1, a2, a3, a4))
print('A ordem de apresentação do trabalho é a seguinte:')
print(turma)
