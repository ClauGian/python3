galera = [['João', 26], ['Maria', 19], ['Pedro', 15], ['Paulo', 32]]
print(galera)
print(galera[0])
print(galera[0][0])
print(galera[2][1])
print(galera[3][0])
print(galera[1][0])
for p in galera:
    print(p)
for p in galera:
    print(p[0])
for p in galera:
    print(p[1])
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade.')
galera = list()
dados = list()
totmai = totmen = 0
for c in range(0, 4):
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Idade: ')))
    galera.append(dados[:])
    dados.clear()
print(galera)
print(dados)
for p in galera:
    if p[1]>= 21:
        print(f'{p[0]} é maior de idade.')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmen += 1
print(f'Temos {totmai} maiores e {totmen} menores de idade.')