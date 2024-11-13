n = int(input('Digite um número: '))
d = n * 2
t = n * 3
r = n ** (1/2)
print('Analisando o número {}: Seu dobro é: {}, seu triplo é: {} e a raiz quadrada dele é: {:.2f}'.format(n, d, t, r))

print('Outra maneira')

print('Analisando o número {}: Seu dobro é: {}, seu triplo é: {} e a raiz quadrada dele é: {:.2f}'.format(n, (n*2), (n*3), (n**(1/2))))


