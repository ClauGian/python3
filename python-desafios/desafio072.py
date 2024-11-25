número = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
n = int(input('Escolha um número entre 0 e 20: '))
while n < 0 or n > 20:
    n = int(input('Número inválido! Digite um número entre 0 e 20. '))

print(f'Você digitou o número → {número[n]}')







