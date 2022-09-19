r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2: #propriedade de um triângulo
    print('Os segmentos acima PODEM FORMAR um triângulo ', end='')
    if r1 == r2 == r3:
        print('EQUILÁTERO')
    elif r1 != r2 != r3 != r1: # r3 diferente de r1 pois todos os lados são diferentes
        print('ESCALENTO')
    else:
        print('ISÓSCELES') # Se não é escaleno nem isósceles ele é escaleno
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo')


# Exercício Python 042: Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
#- EQUILÁTERO: todos os lados iguais
#- ISÓSCELES: dois lados iguais, um diferente
#- ESCALENO: todos os lados diferentes

# O end=' ' serve pra dar continuidade do print na mesma linha