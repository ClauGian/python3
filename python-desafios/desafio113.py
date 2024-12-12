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


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO! Por favor, digite um número Real válido!\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[31mUsuário preferiu não digitar o número.\033[m')
            return '\033[34m→ VAZIO\033[m'
        else:
            return n

n1 = leiaInt('\033[34mDigite um número Inteiro:\033[m ')
n2 = leiaFloat('\033[34mDigite  um  número  Real:\033[m ')
print(f'O valor Inteiro digitado foi {n1} e o Real foi {n2}.')

