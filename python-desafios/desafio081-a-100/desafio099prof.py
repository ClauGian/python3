from time import sleep

def maior(*num):
    cont = mai = 0
    print('~.' * 20)
    print('Analisando os valores fornecidos...')
    for valor in num:
        sleep(.5)
        print(f'{valor}', end=' ')
        if cont == 0:
            mai = valor
        if valor > mai:
            mai = valor
        cont += 1
    print(f'Foram informados {cont} valores.')
    print(f'O maior valor informado foi {mai}.')



#Programa principal.
maior(7, 2, 8, 1, 4, 6)
maior(9, 3, 7)
maior(6, 3)
maior(5)
maior()