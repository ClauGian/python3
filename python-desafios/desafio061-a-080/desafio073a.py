def l ():
    print('._' * 40)
print()
times = ('Palmeiras', 'Botafogo', 'Internacional', 'Fortaleza', 'Flamengo',
         'São Paulo', 'Cruzeiro', 'Bahia', 'Corinthians', 'Atlético-MG',
         'Vasco da Gama', 'EC Vitória', 'Athletico-PR', 'Grêmio', 'Juventude',
         'Fluminense', 'Criciúma', 'Bragantino', 'Cuiabá', 'Atletico-GO')
print(f'{ "TABELA DO BRASILEIRÃO" :=^80}')
for t, v in enumerate(times):
    print(f'{t+1} - {v}')
l()
print(f'Os cinco primeiros colocados são:')
for t in times[:5]:
    print(t)
l()
print(f'Os quatro últimos colocados são:')
for t in times[-4:]:
    print(t)
l()
print(f'Os times em ordem alfabética ficam assim:')
for t in sorted(times):
    print(t)
l()
print(f'O Corinthians esta na {times.index('Corinthians')+1}ª colocação.')
l()
print('Fim da exibição!')



