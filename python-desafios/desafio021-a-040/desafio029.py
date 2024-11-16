vel = float(input('Qual foi a velocidade? '))
multa = (vel - 80) * 7.00
if vel > 80:
    print('O limite de velocidade é de 80Km/h e a sua foi de {}km/h.'.format(vel))
    print('Por isso você foi MULTADO em R$ {:.2f}.'.format(multa))
    print('Use sempre o cinto de segurança e tenha uma boa viagem!')
else:
    print('Sua velocidade foi de {}km/h.'.format(vel))
    print('Use sempre o cinto de segurança e tenha uma boa viagem!')