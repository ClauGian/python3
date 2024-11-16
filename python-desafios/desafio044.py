preco = float(input('Qual o preço do produto? R$ '))
cond = ''
avd = preco - (preco * 10) / 100
avc = preco - ( preco * 5) / 100
c2x = preco
c3x = preco + (preco * 20) / 100
print('O preço do produto é: R$ {:.2f}'.format(preco))
print('Para pgto à vista (dinheiro/cheque), desconto 10%...... = R$ {:.2f}'.format(avd))
print('Para pgto à vista (cartão), desconto de 5%............. = R$ {:.2f}'.format(avc))
print('Para pgto em 2 vezes (cartão).......................... = R$ {:.2f}'.format(preco))
print('Para pgto em 3 vezes ou mais (cartão), acréscimo de 20% = R$ {:.2f}'.format(c3x))