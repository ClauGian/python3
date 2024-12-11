import moeda
from moeda import dobro, metade, aumentar, diminuir

p = float(input('Digite um preço: R$ '))
print(f'A metade de {moeda.moeda(p)} é {metade(p, True)}')
print(f'O dobro de {moeda.moeda(p)} é {dobro(p, True)}')
print(f'Aumentando 10% temos {aumentar(p, 10, True)}')
print(f'Reduzindo 13% temos {diminuir(p, 13, True)}')
