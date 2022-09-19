número = int(input('Me diga um número qualquer: '))
resultado = número % 2
if resultado == 0:
    print(f'o número {número} é par')
else:
    print(f'O número {número} é ímpar')

# Exercício Python 030: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
# LINHA 2 >>> Verifica se o resto do número é 0 (par) ou 1 (ímpar) pela % 2
# LINHA 3 >>> Dentro da condição se o resultado for 0 o número é par senão é ímpar