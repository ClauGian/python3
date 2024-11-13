print('{:=^40}'.format(' L O C A D O R A '))
dias = int(input('Quantos dias alugado? '))
km = float(input('Quantos km percorridos? '))
pgto = (dias * 60.00) + (km * 0.15)

print('O custo do aluguel foi de: R$ {:.2f}'.format(pgto))
