núm = int(input('Digite um número: '))
total = 0 # total (quantas vezes o número é divisivel)
for c in range(1, núm +1): # o núm digitado até ele mesmo +1 pois só vai até ele mesmo -1
    if núm % c == 0: # se o núm for divisível pelo contador
        print('\33[33m', end='') # código de cor (mundo  do curso em vídeo)
        total += 1
    else:
        print('\33[31m', end='') # o end serve pra continuar na mesma linha
# O esquema de cores em amarelo são os números que podem ser divisíveis
    print(f'{c}', end='' )
print(f'\n\033[m O número {núm} foi divisível {total} vezes')
if total == 2: # é primo se for divisível por 1 e por ele mesmo. 2 n° divisíveis
    print('É um número PRIMO')
else: # se mais de dois números divisíveis ele não é primo
    print('Não é um número PRIMO')


# Exercício Python 052: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo. 