# Tuplas são imutáveis (não se pode adicionar mais elementos).
lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
print(lanche)
print('-1--')
print(lanche[1])
print('-2--')
print(lanche[0])
print('-3--')
print(lanche[2])
print('-4--')
print(lanche[3])
print('-5--')
print(lanche[-1])
print('-6--')
print(lanche[1:3]) #Ele busca só o elemento 1 e 2.
print('-7--')
print(lanche[2:]) # Vai do elemento 2 até fim.
print('-8--')
print(lanche[:2]) # vai do inicio até o elemento 1
print('-9--')
print()
print('-10-- Usando o → sorted ← ele ordena a tupla só na exibição, o arquivo é imutável.')
print(sorted(lanche))
print(lanche)
print()
for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Ufa! comi demais.')
print()

for cont in range(0, len(lanche)):
    print(f'Eu vou comer em {cont+1}º → {lanche[cont]}')
print()
a = (2, 4, 6)
b = (3, 5, 7, 9)
c = (a + b)
print(a)
print(b)
print(c)
print()
n = (2, 4, 6, 8)
print(n)
del n
print(n)# este comando print da erro, diz que tupla não foi encontrada.

