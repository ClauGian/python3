produto = ''
preço = ''
for c in range(1 , 4):
    prod = str(input('Produto: '))
    pre = str(input('Preço: R$ '))
    produto = produto + prod
    preço = preço + pre

    print(' = ' * 10)
print('{:.20} e o preço R$ {}'.format(produto, preço))

#print(preço)