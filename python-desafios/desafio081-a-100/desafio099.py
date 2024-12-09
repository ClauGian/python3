from random import randint
from time import sleep

def maior(*num):
    sleep(.5)
    mai = max(num)
    print('==' * 20)
    print('....Analisando os valores informados....')
    print(f' - Os valores são: {num}.')
    print(f' - Foram informados {len(num)} valores ao todo.')
    print(f' - O maior valor informado foi {mai}')


maior(randint(0, 10), randint(0, 10), randint(0, 10),
      randint(0, 10), randint(0, 10), randint(0, 10))

maior(randint(0, 10), randint(0, 10), randint(0, 10))

maior(randint(0, 10), randint(0, 10))

maior(randint(0, 10))

maior(0)


