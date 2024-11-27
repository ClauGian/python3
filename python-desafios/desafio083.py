
form = str(input('Digite uma equação matemática: '))
if form.count('(') == form.count(')'):
    print('Esta equação está correta!')
else:
    print('Esta equação está errada! Verifique os parênteses.')