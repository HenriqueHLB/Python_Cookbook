import random

c1 = input('Primeira coisa: ')
c2 = input('Segunda coisa: ')
print('\n')

sorteio = random.choice([c1, c2])

print(f'Resultado: {sorteio}')