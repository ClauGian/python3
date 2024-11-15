"""
nome = str(input('Qual é o seu nome? '))
if nome == 'Claudinei':
    print('Que nome lindo você tem!')
else:
    print('É um nome bem comum!')
print('Bom dia {}'.format(nome))"""

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print('Sua média foi de: {:.2f}'.format(m))
if m >= 7:
    print('Você foi APROVADO!')
else:
    print('Infelizmente você foi REPROVADO!')
print('===FIM===')