soma = 0 # acumulador
cont = 0 # contador
for c in range(1,501,2):       # listar impares entre 1 e 500
    if c % 3 == 0:             # listar múltiplos de 3
        soma += c # soma os valores respectivamente (soma = soma + c)
        cont += 1 # conta mais um número 01 (cont = cont + 1)
        #print(c, end=' ') mostra todos os números da solução
print(f'A soma de todos os {cont} valores solicitados é {soma}')

    
# Exercício Python 048: Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.