palavra = input('Palavra: ')

if palavra == palavra[::-1]:
    print('É palíndromo.')
else:
    print('Não é palíndromo.')