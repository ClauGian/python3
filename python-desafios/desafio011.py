larg = float(input('Informe a largura da parede: '))
alt = float(input('Informe a altura da parede: '))
area = larg * alt
tinta = 2
litros = area / tinta
print('A sua área é de {:.1f} metros quadrados.'. format(area))
print('Para pintar essa área, serão necessários {:.1f} litros de tinta'.format(litros))


