from collections import Counter


frase = input('Frase: ')
print('\n')

contagem = dict(Counter(frase.split()))

for x in contagem:
    print(f'{x}: {contagem[x]}')