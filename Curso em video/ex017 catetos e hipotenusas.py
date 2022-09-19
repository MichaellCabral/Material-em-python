#Exercício Python 017: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
# O quadrado da hipotesusa é igual a soma dos quadrados dos catetos
"""
catetooposto = (eval(input(f'comprimento do cateto oposto: ')))
catetoadjacente = (eval(input(f'comprimento do cateto adjacente: ')))

hipotenusa = (catetooposto **2 + catetoadjacente **2) ** (1/2) # tudo elevado a meio pra descobrir a raiz quadrada de um numero
print(f'A hipotenusa do triangulo equivale a : {hipotenusa:.2f}')
"""
"""
# AGORA COM IMPORTAÇÃO DA CLASS MATH
import math
catetooposto = (eval(input(f'comprimento do cateto oposto: ')))
catetoadjacente = (eval(input(f'comprimento do cateto adjacente: ')))

hipotenusa = math.hypot(catetooposto,catetoadjacente)
print(f'A hipotenusa vai medir: {hipotenusa:.2f}')
"""

# AGORA COM IMPORTAÇÃO DA CLASS MATH SOMENTE COM A HIPOTENUSA
from math import hypot
catetooposto = (eval(input(f'comprimento do cateto oposto: ')))
catetoadjacente = (eval(input(f'comprimento do cateto adjacente: ')))

hipotenusa = hypot(catetooposto,catetoadjacente)
print(f'A hipotenusa vai medir: {hipotenusa:.2f}')