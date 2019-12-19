import random


print('Bem-vindo ao jogo da advinhação! Um número aleatório de 1 a (um número de sua escolha) será gerado, você terá que acertar ele.\n\n\n')

ganhou = False
tentativas = 0
nmax = int(input('Gerar um número aleatório de 1 a '))
print('\n')
n = random.randint(1, nmax)

while ganhou != True:
    chute = int(input('Chute: '))
    tentativas += 1

    if chute == n:
        print(f'\n\nParabéns, você ganhou! Tentativas: {tentativas}.')
        ganhou = True
    elif chute > n:
        if chute > nmax:
            print(f'O número máximo do sorteio é {nmax}. Você não pode ultrapassar ele.\n')
            tentativas -= 1
        else:
            print('Você errou. Tente um número menor dessa vez.\n')
    elif chute < n:
        print('Você errou. Tente um número maior dessa vez.\n')