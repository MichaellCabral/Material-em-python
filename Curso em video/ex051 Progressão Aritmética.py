cont=0
primeiro = int(input('Primeiro termo: '))
razao=int(input('Razão: '))
décimo = primeiro + (10 - 1) * razao # fórmula do enésimo número de uma p.a
for c in range(primeiro, décimo + razao, razao):
    cont+=1
    print(f'{cont}° número = {c}')
print('ACABOU')



# Exercício Python 051: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.