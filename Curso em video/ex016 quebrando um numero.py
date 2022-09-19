#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira. 
"""import math #biblioteca para operações matematicas
num = eval(input('digite um numero qualquer: '))
print (f'o número digitado foi {num} e sua porção inteira é: {math.trunc(num)}')  #math .trunc mosta a parte inteira de um número"""

#FAZENDO DE OUTRA MANEIRA
num  = float(input('digite um valor: '))
print(f'O valor digitado foi {num} e a sua porção inteira é: {int(num)}')