n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
med = (n1 + n2) / 2
if med <= 5:
    print('Média:\033[1;31m {}\033[m = Status: \033[1;31mREPROVADO\033[m.'.format(med))
elif med < 7:
    print('Média:\033[1;36m {}\033[m = Status: \033[1;36mEM RECUPERAÇÃO\033[m.'.format(med))
elif med <= 9:
    print('Média:\033[1;34m {}\033[m = Status: \033[1;34mAPROVADO\033[m.'.format(med))
else:
    print('Média:\033[1;34m {}\033[m = Status: \033[1;34mAPROVADO COM LOUVOR\033[m.'.format(med))
