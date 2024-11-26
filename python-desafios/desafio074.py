from random import randint

números = (randint(0, 9), randint(0, 9), randint(0, 9),
           randint(0, 9), randint(0, 9))
menor = min(números)
maior = max(números)
print(f'Os números sorteados são: {números}.')
print(f'O maior número sorteado foi {maior}.')
print(f'O menor número sorteado foi {menor}.')
