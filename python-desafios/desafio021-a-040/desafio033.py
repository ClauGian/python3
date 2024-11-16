n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))
""" PRIMEIRA FORMA E MAIS SIMPLES PARA RESOLVER
lista = [n1, n2, n3]
print('O MENOR número digitado foi: {}'.format(min(lista)))
print('O MAIOR número digitado foi {}.'.format(max(lista)))"""

#FORMA USANDO CONDICIONAL
# Determinando o MENOR
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
# Determinando o MAIOR
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3

print('O MENOR número digitado foi: {}'.format(menor))
print('O MAIOR número digitado foi {}.'.format(maior))








