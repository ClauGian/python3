from moeda import dobro, metade, aumentar, diminuir

p = float(input('Digite um preço: R$ '))
print(f'A metade de R$ {p} é R$ {metade(p)}')
print(f'O dobro de R$ {p} é {dobro(p)}')
print(f'Aumentando 10% temos R$ {aumentar(p, 10)}')
print(f'Reduzindo 13% temos R$ {diminuir(p, 13)}')
