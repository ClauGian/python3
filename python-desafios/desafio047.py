print('Os números pares 1 a 50 são:')
for c in range(1, 51):
    print(' - ', end='')
    if c % 2 == 0:
        print(c, end='' )
print()
# No primeiro caso ele faz duas interações, já no segundo uma só. Veja pelo traço.
for i in range(2, 51, 2):
    print(' - ', end='')
    print(i, end='' )
