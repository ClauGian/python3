cad = {}
cad['nome'] = str(input('Nome: '))
media = float(input(f'Média de {cad['nome']}: '))
cad['media'] = media
if media > 7:
    sit = 'APROVADO'
    cad['situação'] = 'APROVADO'
else:
    sit = 'REPROVADO'
    cad['situação'] = 'REPROVADO'

print(f'Nome é igual a {cad['nome']}.')
print(f'Média é igual a {cad['media']}.')
print(f'Situação é igual a {cad['situação']}.')
print()
print(f'Aluno {cad['nome']} com média {cad['media']} esta {sit}.')
print(cad)