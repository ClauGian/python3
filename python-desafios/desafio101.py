
def voto(votar):
    from datetime import date
    ano = date.today().year
    idade = ano - nasc
    if idade < 16:
        return f'Com {idade} anos, "NÃO PODE VOTAR".'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos, "PODE VOTAR, MAS É FACULTATIVO".'
    elif 18 <= idade <= 65:
        return f'Com {idade} anos, "O VOTO É OBRIGATÓRIO".'


nasc = int(input('Em que ano você nasceu? '))

print(voto(nasc))


