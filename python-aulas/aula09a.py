frase = 'Curso em Vídeo Python'
print('FATIAMENTO')
print(frase)
print(frase[3]) # mostra a letra na posição 3
print(frase[3:13]) # mostra a letra na posição 3 até a posição 12
print(frase[:13]) # mostra do início até a posição  12
print(frase[13:]) # mostra da posição 13 até fim
print(frase[1:15:2]) # mostra da posição 1 até a 14 pulando 2 casas
print(frase[0::2]) # mostra da posição 0 até o fim pulando 2 casas
print(frase[::3]) # mostra da posição 0 até o fim pulando 3 casas
print('ANALISE')
print(len(frase)) # mostra o tamanho da string (SERÁ MUITO USADA)
print(frase.count('o')) # mostra quantas letras 'o' tem
print(frase.count('o', 0, 13)) # letra 'o' de 0 a 12
print(frase.find('deo')) # mostra onde inicia a palavra 'deo'
print(frase.find('Android')) # tem 'android' resp. -1
print('curso' in frase) # pergunta se tem android na frase
print('TRANSFORMAÇÃO')
print(frase.replace('Python', 'Android'))
print(frase) # só substitui no comando, a frase permanece a mesma.
print(frase.upper()) # Passa tudo para maiuscula.
print(frase.lower()) # Passa tudo para minuscula.
print(frase.capitalize()) # Somente a primeira letra da string em maiuscula
print(frase.title()) # Coloca as iniciais de cada palavra em maiuscula
frase = '    Curso em Vídeo Python   '
print(frase)
print(frase.strip()) # Elimina os espaços vazios no inicio e no fim
print(frase.rstrip()) # Elimina os espaços da direita 'r' de right
print(frase.lstrip()) # Elimina os espaços da esquerda 'l' de left
print('DIVISÃO')
frase = 'Curso em Vídeo Python'
print(frase.split()) # transforma a string em ula lista palavra por palavra
print('JUNÇÃO')
frase = 'Curso em Vídeo Python'
print('-'.join(frase.split())) # faz uma junção entre as palavras
print('-'.join(frase)) # adiciona um hifem entre cada letra e intervalos


