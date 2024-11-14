print('Quanto custa esse produto?')
vlr = float(input('Esse produto custa R$ '))
desc = 5
vcd = vlr - (vlr * 5 / 100)
print('Mas com o desconto de 5% ele sai por {:.2f}'.format(vcd))
