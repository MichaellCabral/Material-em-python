casa = float(input('Valor da casa: R$'))
salário = float(input('Salário do comprador: R$'))
anos = int(input('Quanto anos de financiamento? '))
prestação = casa  / (anos * 12)
mínimo = salário * 30/100 # o salário multipicado por 30% (30 / 100) é o mínimo
# prestação é o valor da casa dividido pela quantidade de meses(ano multiplicado por 12)
print(f'Para pagar uma casa de R${casa:.2f} em {anos} anos', end='') # End faz a linha continuar na próxima linha digitável
print(f' a prestação será de R${prestação:.2f}')

print(f'Comparando tem que pagar {prestação} e o mínimo é de {mínimo}')

if prestação <= mínimo:
    print('Empréstimo pode ser CONCEDIDO')
else:
    print('Empréstimo NEGADO')


# Exercício Python 036: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.