from datetime import date
anoa = date.today().year
anon = int(input('Em que ano você nasceu? '))
idade = anoa - anon
menor = (-idade) + 18
maior = idade - 18
quando = anon + 18
if idade < 18:
    print('=>\033[1;31m Você tem {} anos.\033[m \033[1;34mAinda faltam {} anos para se alistar.\033[m'.format(idade, menor))
    print('=>\033[36m Você vai se alistar somente em {}.\033[m'.format(quando))
elif idade == 18:
    print('=>\033[1;31m Você tem {} anos.\033[m \033[4;30;42mEstá na hora de se alistar.\033[m'.format(idade))
else:
    print('=>\033[1;31m Você tem {} anos.\033[m \033[1;34mJá se passaram {} anos do seu alistamento.\033[m'.format(idade, maior))
    print('=>\033[36m Você deveria ter se alistado em {}.\033[m'.format(quando))
