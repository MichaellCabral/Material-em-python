from cmath import sin
import math
angulo = float(input('Digite o angulo que você deseja: '))
seno = math.sin(math.radians(angulo)) #o angulo digitado é convertido pra radianos e calculado o seno - segue a sequencia dos parenteses
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print(f'O seno é igual a: {seno:.2f}\nO cosseno é igual a: {cosseno:.2f} \nA tangente é igual a: {tangente:.2f}')






#Exercício Python 018: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.