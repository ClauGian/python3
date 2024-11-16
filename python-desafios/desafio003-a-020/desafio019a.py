import random
a1 = 'Paulo'
a2 = 'José'
a3 = 'Marcos'
a4 = 'Claudinei'
turma = [a1, a2, a3, a4]
sorteio = random.choice(turma)
print('O aluno sorteado foi: {}'.format(sorteio))