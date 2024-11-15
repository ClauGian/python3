n = int(input('\033[34mDigite um número:\033[m '))
if n % 2 == 0:
    print('O número {} é \033[30;43mPAR\033[m.'.format(n))
else:
    print('O número {} é \033[30;46mIMPAR\033[m.'.format(n))

