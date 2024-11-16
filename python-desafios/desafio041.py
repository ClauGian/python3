from datetime import date
anoa = date.today().year
anon = int(input('Qual o ano de nascimento? '))
idade = anoa - anon
if idade <= 9:
    print('Idade: \033[31m{} anos\033[m. Categoria: \033[34mMIRIM\033[m'.format(idade))
elif idade <= 14:
    print('Idade: \033[31m{} anos\033[m. Categoria: \033[34mINFANTIL\033[m'.format(idade))
elif idade <= 18:
    print('Idade: \033[31m{} anos\033[m. Categoria: \033[34mJUNIOR\033[m'.format(idade))
elif idade <= 20:
    print('Idade: \033[31m{} anos\033[m. Categoria: \033[34mSENIOR\033[m'.format(idade))
else:
    print('Idade: \033[31m{} anos\033[m. Categoria: \033[34mMASTER\033[m'.format(idade))