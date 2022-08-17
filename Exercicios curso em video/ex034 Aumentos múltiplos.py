salário =  float(input('Qual é o salário do funcionário?'))
if salário <= 1250:
    novo = salário + (salário * 15/100) # inferior ou igual a 1250 aumneta 15%, entre parenteses esta o calculo de 15%
else:
    novo = salário + (salário * 10/100) # acima de 1250 soma com 10% do salario
print(f'Quem ganhava R${salário:.2f} passa a ganhar R${novo:.2f}')


# Exercício Python 034: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

# Temos aqui uma forma de calcular porcentagem. Exercite!