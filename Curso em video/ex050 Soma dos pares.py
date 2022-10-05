soma = 0 #acumulador
cont = 0 #contador
for c in range(1,7):
    num = int(input(f'Digite o {c}° valor: ')) # o "c" mostra o número da contagem
    if num % 2 == 0: # CONDIÇÃO = SE FOR PAR SOMA E CONTA (abaixo)
        soma += num
        cont += 1
print(f'Você informou {cont} números PARES e a soma foi {soma}') # Mostra somente a contagem dos n° pares e a soma deles


# Exercício Python 050: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.