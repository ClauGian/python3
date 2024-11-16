nome = str(input('Nome completo: '))
vcasa = float(input('Qual o valor do imóvel? R$ '))
sal = float(input('Qual é o seu salário? R$ '))
prazo = int(input('Em quantos anos pretende financiar? Anos: '))
qprest = prazo * 12
vprest = vcasa / qprest
sal30 = (sal * 30) / 100
print('            \033[30;43mRESUMO\033[m')
print('\033[1;35m===\033[m' * 15)
print('Nome: {}'.format(nome))
print('Valor do imóvel:..........R$ {:.2f}'.format(vcasa))
print('Prazo do financiamento:...   {} meses'.format(qprest))
print('Valor da prestação:.......R$   {:.2f}'.format(vprest))
print('Renda:....................R$   {:.2f}'.format(sal))
if vprest > sal30:
    print('\033[30;41m= NEGADO =\033[m O valor da prestação ultrapassa 30% de sua renda.')
else:
    print('\033[1;30;43mSEU FINANCIAMENTO FOI APROVADO!\033[m')



