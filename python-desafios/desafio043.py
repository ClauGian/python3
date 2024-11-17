peso = float(input('Qual é o seu peso? Kg: '))
alt = float(input('Qual é a sua altura? m: '))
imc = peso / (alt ** 2)
print('Com peso de {:.1f}kg e altura de {:.2f}m.'.format(peso, alt))
if imc < 18.5:
    print('Seu IMC é \033[34m{:.1f}\033[m. Você está \033[34mAbaixo do Peso Ideal\033[m.'.format(imc))
elif imc < 25:
    print('Seu IMC é \033[34m{:.1f}\033[m. PARABÉNS. Você está no \033[34mPeso Ideal\033[m.'.format(imc))
elif imc < 30:
    print('Seu IMC é \033[34m{:.1f}\033[m. Sua situação é de \033[34mSobrepeso\033[m.'.format(imc))
elif imc <= 40:
    print('Seu IMC é \033[34m{:.1f}\033[m. Sua situação é de \033[34mObesidade\033[m.'.format(imc))
else:
    print('Seu IMC é \033[34m{:.1f}\033[m. Sua situação é de \033[34mObesidade Mórbida\033[m.'.format(imc))
