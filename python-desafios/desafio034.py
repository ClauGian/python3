sal = float(input('Qual é o valor de seu salário? R$ '))
aumento = 0
if sal <= 1250.00:
    aumento = (sal * 15) / 100
    print('Seu salário é de R$ {:.2f} e recebeu um AUMENTO de 15% R$ {:.2f}, passando para R$ {:.2f}.'.format(sal, aumento, (sal + aumento)))
else:
    aumento = (sal * 10) / 100
    print('Seu salário é de R$ {:.2f} e recebeu um AUMENTO de 10% R$ {:.2f}, passando para R$ {:.2f}.'.format(sal, aumento, (sal + aumento)))
