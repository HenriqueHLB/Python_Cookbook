import sys

try:
    print(f'O argumento foi: {sys.argv[1]}')
except IndexError:
    print('Você não forneceu nenhum argumento.')