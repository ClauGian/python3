qh = qm = idade = qi = 0
res = ''
sexo = ''
while res != 'N':
    print('==' * 15)
    print('{:^30}'.format('CADASTRO PESSOAL'))
    print('==' * 15)
    idade = int(input('Qual é a sua idade: '))
    sexo = str(input('Qual sexo? [M / F]: ')).upper().strip()
    while sexo != 'M' and sexo != 'F':
        sexo = str(input('Qual sexo? [M / F]: ')).upper()
    if idade > 18:
        qi += 1
    if sexo == 'M':
        qh += 1
    if sexo == 'F' and idade <= 20:
        qm += 1
    print('..' * 15)
    res = str(input('Deseja continuar? [S / N]: ')).upper().strip()
    if res != 'S' and res != 'N':
        res = str(input('Deseja continuar? [S / N]: ')).upper().strip()
print(f'Foram cadastradas {qi} pessoas com mais de 18 anos.')
print(f'Ao todo temos {qh} pessoas do sexo masculino.')
print(f'Temos também {qm} mulheres com menos de 20 anos.')