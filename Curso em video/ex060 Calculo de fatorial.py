#Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial.
#Com módulo math    
"""
from math import factorial
n = int(input('Digite um numero para calcular o seu fatorial: '))
f = factorial(n) # calcula o fatorial de do numero digitado
print(f'O fatorial de {n} é {f}')
"""

# Forma tradicional
n = int(input('Digite um numero para calcular o seu fatorial: '))
c = n
f = 1
print(f'Calculando {n}! =', end='')
while c > 0:
    print(f'{c}', end='') # end='' pra que os numero aparecam na mesma linha
    print('x' if c > 1 else '=', end='') # Se o contaodor for maior que 1 seja 'x' senão '='
    f *= c
    c -= 1
print(f'{f}')

    
