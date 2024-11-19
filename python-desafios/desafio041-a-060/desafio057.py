M = 'Masculino'
F = 'Feminino'
c = 1
sexo = str(input('Qual é seu sexo? [M / F]: '))
while sexo == 'm' or sexo == 'f':
    sexo = str(input('ERRO! Digite novamente! '))
    c += 1
print('Ok, Você digitou corretamente.')

print('Fim')