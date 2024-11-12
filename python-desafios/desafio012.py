vlr = float(input('Quanto custa esse produto? '))
desc = (vlr * 5) / 100
vcd = vlr - desc
print('Este produto tem desconto de 5% que é {:.2f} e sai por {:.2f}'.format(desc, vcd))
