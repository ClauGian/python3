sal = float(input('Qual seu salário atual? R$ '))
aum = (sal * 15) / 100
salat = sal + aum
print('{:=^80}'.format(' P A R A B É N S '))
print('Seu salário teve aumento de 15% no valor de R$ {:.2f}, passando para R$ {:.2f}'.format(aum, salat))
