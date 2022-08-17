print('-='*20)
print('Analisador de triangulos')
print('-='*20)
r1 = float(input('primeiro segmento: '))
r2 = float(input('segundo segmento: '))
r3 = float(input('terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR triângulo!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo')


# Exercício Python 035: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

# FÓRMULA: r1 tem que ser igual a soma do comprimento do r2 e r3
# Cada segmento tem que ser menor que a soma dos outros dois segmentos
# Esse exercício é melhorado em outro ex a frente onde mostra o tipo de triangulo que foi formado