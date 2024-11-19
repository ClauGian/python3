print('{:#^70}'.format('\033[30;42m  L O J A S    C  &  G  \033[m'))
preço = float(input('Qual o da sua compra? R$ '))

print('''\033[4;34mFORMAS DE PAGAMENTO\033[m
[ 1 ] À vista (dinheiro ou cheque).
[ 2 ] Á vista no cartão.
[ 3 ] 2 vezes no cartão.
[ 4 ] 2 vezes ou mais no cartão.''')
opção = int(input('Qual é sua opção? '))
if opção == 1:
    total = preço - (preço * 10) / 100
elif opção == 2:
    total = preço - (preço * 5) / 100
elif opção == 3:
    total = preço
    parc = preço / 2
    print('Sua compra será parcelada em 2 vezes de R$ {:.2f} SEM JUROS'.format(parc))
elif opção == 4:
    total = preço + (preço * 20) / 100
    qtde = int(input('Em quantas vezes deseja parcelar? '))
    parc = total / qtde
    print('Sua compra será parcelada em {} vezes de R$ {:.2f} COM JUROS'.format(qtde, parc))
else:
    total = preço
    print('OPÇÃO INVÁLIDA de pagamento. Tente novamente!')
print('Sua compra no valor total de R$ {:.2f}, vai custar R$ {:.2f} no final.'.format(preço, total))
