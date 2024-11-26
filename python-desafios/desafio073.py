print()
times = ('Palmeiras', 'Botafogo', 'Internacional', 'Fortaleza', 'Flamengo',
         'São Paulo', 'Cruzeiro', 'Bahia', 'Corinthians', 'Atlético-MG',
         'Vasco da Gama', 'EC Vitória', 'Athletico-PR', 'Grêmio', 'Juventude',
         'Fluminense', 'Criciúma', 'Bragantino', 'Cuiabá', 'Atletico-GO')
print('-:-' * 15)
print(f'\033[34mA lista dos times do Brasileirão:\033[m {times}.')
print('-:-' * 15)
print(f'\033[34mOs cinco primeiros colocados são:\033[m {times[0:5]}.')
print('-:-' * 15)
print(f'\033[34mOs quatro últimos colocados são:\033[m {times[-4:]}.')
print('-:-' * 15)
print(f'\033[34mA relação dos times em ordem alfabética:\033[m {sorted(times)}.')
print('-:-' * 15)
print(f'\033[34mO Corinthians está na {times.index('Corinthians')+1}ª posição.\033[m')



