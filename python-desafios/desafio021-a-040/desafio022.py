nome = str(input('Digite seu nome completo: '))
print('Seu nome é: ',nome)
print('Seu nome em letras maiusculas: {}.'.format(nome.upper()))
print('Seu nome em letras minusculas: {}.'.format(nome.lower()))
print('Seu nome com espaços possui {} caracteres.'.format(len(nome)))
print('Seu nome sem espaços possui {} caracteres.'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome é: {}.'.format(nome.split()[0]))
print('Seu primeiro nome possui {} caracteres.'.format(len(nome.split()[0])))
print('Seu sobrenome é: {}.'.format(nome.split()[-1]))
print('Seu sobrenome possui {} caracteres.'.format(len(nome.split()[-1])))


