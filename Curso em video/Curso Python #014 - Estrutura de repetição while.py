"""
# LAÇO FOR - DE 1 A 10
for c in range(1,11):
    print(c)
print('Fim')
"""

"""
# LAÇO WHILE - DE 01 A 10 
c = 1 # contador, pos começa a partir do número "1"
while c < 10:
    print(c)
    c += 1 # Soma mais
print('Fim')
"""


"""
# LAÇO FOR - DE 1 A 3 COM LIMITE DE NÚMEROS
for c in range(1,4):
    n = int(input('Digite um número: '))
print('Fim')
"""

"""
#WHILE - ENQUANTO DIFERENTE DE "0" SEM LIMITE
n = 1
while n != 0: # enquanto n for diferente de 0: "FLAG" (condição de parada ou ponto de parada)
    n = int(input('Digite um valor: ')) # digite o valor infinitamente
print('Fim')
"""

"""
# WHILE - ENQUANTO "S" CONTINUA E "N" PARA O LAÇO
r = 'S'
while r == 'S': # enquanto r == "S": continue 
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N] ')).upper() # .upper() = transforma o S em minuscula ou maiscula
print('Fim')
"""

n = 1 
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0: # Se o "n" for diferente de zero funciona o laço abaixo
        if n % 2 == 0: # se o número for par (resto da divisão por 2 igual a zero) então
            par += 1 # numero par soma mais 01 no laço
        else: # se não for par (é ímpar) então:
            impar += 1
print(f'Você digitou {par} numeros pares e {impar} números ímpares!')