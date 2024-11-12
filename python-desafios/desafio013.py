sal = float(input('Qual seu salário atual? '))
aum = (sal * 15) / 100
salat = sal + aum
print('Seu salário teve aumento de 15% no valor de R$ {:.2f}, passando para R$ {:.2f}'.format(aum, salat))
