def notas(*n, sit=False):
    """
    → Função para analizar a situação de vários alunos.
    :param n: Uma ou mais notas do aluno (aceita várias).
    :param sit: Valor opcional indicando se deve ou não adicionar a situação.
    :return: Dicionário com várias informações sobre a situação da turma.
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n) / len(n)
    if sit:
        if r['media'] >= 7:
            r['situação'] = 'BOA'
        elif r['media'] >= 5:
            r['situação'] = 'RAZOAVEL'
        else:
            r['situação'] = 'RUIM'

    return r

#Programa principal:
resp = notas(7, 8, 9, sit=True)
print(resp)