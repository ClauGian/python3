def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO! Por favor, digite um número Inteiro válido!\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[31mUsuário preferiu não digitar o número.\033[m')
            return '\033[34m→ VAZIO\033[m'
        else:
            return n

def linha(tam=42):
    return '\033[34m~\033[m' * tam

def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

def menu(lista):
    cabeçalho('\033[32mMENU PRINCIPAL\033[m')
    c = 1
    for item in lista:
        print(f'\t{c}  -  {item}')
        c += 1
    print(f'{linha()}')
    opc = leiaInt('\t\033[34mSua Opção: \033[m')
    return opc


