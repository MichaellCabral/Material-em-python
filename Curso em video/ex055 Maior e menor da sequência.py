maior = 0
menor = 0
for p in range(1,6): 
    peso = float(input(f'Peso da {p}° pessoa: ')) # "p" serve de contador
    if p == 1: # o 1° laço recebe o maior e o menor peso
        maior = peso
        menor = peso
    else: # se não for o 1° laço então:
        if peso > maior: # se o peso for maior que valor de "maior" então:
            maior = peso # maior recebe o valor de peso
        if peso < menor: # se o peso for menor que valor de  "menor" então:
            menor = peso # menor recebe o valor de peso
print(f'O maior peso lido foi de {maior}Kg')
print(f'O menor peso lido foi de {menor}Kg')


# Exercício Python 055: Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.