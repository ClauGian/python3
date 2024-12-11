from time import sleep
c = ('\033[m',      # 0 - sem cores
     '\033[1;30;41m', # 1 - Vermelho
     '\033[1;30;42m', # 2 - Verde
     '\033[1;30;43m', # 3 - Amarelo
     '\033[1;30;44m', # 4 - Azul
     '\033[1;30;45m', # 5 - Roxo
     '\033[1;30;46m', # 6 - lilas
     '\033[1;30;47m', # 7 - Não sei
     '\033[7;40m',  # 8 - Branco
)
def ajuda(com):
    título(f'   Acessando o manual do comando {"com"}   ', 6)
    sleep(1.2)
    print(c[8], end='')
    help(com)
    print(c[0], end='')
    sleep(1)

def título(msg, cor=0):
    tam = len(msg)
    sleep(1.2)
    print(c[cor], end='')
    print('~' * tam)
    print(msg)
    print('~' * tam)
    print(c[0], end='')

#Programa principal:
comando = ''
while True:
    título('    SISTEMA DE AJUDA Py-HELP    ', 2)
    comando = str(input('[FIM para sair] Função ou Biblioteca? '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
título('    Até Logo    ', 1)




"""def sist(msg):
    print('\033[30;43m~' * len(msg))
    print(f'\033[30;45m{msg}')
    print('\033[30;43m~' * len(msg))


def man(msg):
    print('\033[30;41m~' * len(msg))
    print(f'\033[30;44m{msg}')
    print('\033[30;41m~' * len(msg))

while True:
    sist('    SISTEMA DE AJUDA Py-HELP    ')
    print('\033[m')
    nome = str(input('Função ou Biblioteca ("Fim" para sair) > '))
    if nome in 'fimFimFIM':
        break
    print()
    sleep(.5)
    man(f'    Acessando o manual do comando "{nome}"    ')
    sleep(1)
    print('\033[m] \033[30;47m')
    print(f'{help(nome)}')
    print('\033[m')
    sleep(1)
"""







