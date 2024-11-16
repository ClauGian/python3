larg = float(input('Informe a largura da parede: '))
alt = float(input('Informe a altura da parede: '))
area = larg * alt
tinta = 2
litros = area / tinta
print('Suas paredes tem as dimensões de {:.2f}m X {:.2f}m que nos dá uma área de {:.2f} m².'.format(larg, alt, area))
print('Para pintar essa área, serão necessários {:.2f} litros de tinta'.format(litros))


