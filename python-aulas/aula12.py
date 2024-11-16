nome = str(input('Qual é o seu nome? '))
if nome == 'Claudinei':
    print('Que nome bonito')
elif nome == 'Maria' or nome == 'José' or nome == 'Paulo':
    print('Seu nome é bem comum no Brasil.')
elif nome in 'Paula Claudia Jéssica Diana':
    print('{} é um nome feminino muito bonito'.format(nome))
else:
    print('{} é um nome comum.'.format(nome))
print('Tenha um bom dia, {}!'.format(nome))