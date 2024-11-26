n = [2, 5, 4, 9]
print(n)
n[2] = 8
print(n)
n.append(7)
print(n)
n.sort()
print(n)
n.sort(reverse=True)
print(n)
print(f'Essa lista tem {len(n)} elementos.')
n.insert(2, 0)# Insere o nº 0 na posição 2
print(n)
n.pop()# Elimina o ultimo elemento no caso o 2.
print(n)
n.pop(2) # Elimina o segundo elemento que no caso é o 0.
print(n)
#n.pop(4)
#print(n) #retorna IndexError: a lista não tem o elemento 4
n.insert(2, 5)
print(n)
n.remove(5)# Removeu o primeiro elemento 5
print(n)
if 4 in n:
    n.remove(4)
else:
    print('Não achei o número 4')
    print()
print('Minha nova lista')
valores = list()
valores.append(7)
valores.append(6)
valores.append(5)
print(valores)
for c, v in enumerate(valores):
    print(f'Na posição {c} tenho o valor {v}')
print('Cheguei ao final da lista!')
print()
print('Novo for')
for c in range(1, 6):
    valores.append(int(input('Digite um valor: ')))
print() # Ele juntou as duas listas em uma só sequência.
for c, v in enumerate(valores):
    print(f'Na posição {c} tenho o valor {v}')
print('Cheguei ao final da lista!')
print()
print('NOvo caso')
a = [2, 3 , 4, 5]
b = a
print(f'Lista A = {a}')
print(f'Lista B = {b}')
b[2] = 9 #===> Ao mandar substituir o 4 po 9 na lista b ele substitui nas duas.
print(f'Lista A = {a}')
print(f'Lista B = {b}')
print('NOvo caso')
a = [2, 3 , 4, 5]
b = a[:] #===> É copiado o conteudo de a em b
print(f'Lista A = {a}')
print(f'Lista B = {b}')
b[2] = 9 #===> Ao mandar substituir o 4 po 9 na lista b ele substitui somente na b.
print(f'Lista A = {a}')
print(f'Lista B = {b}')
