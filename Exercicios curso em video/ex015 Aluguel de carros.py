# Qual a quantidade de km percorridos pelo carro alugado e a quantidade de dias que ele foi alugado?
# Calcule o preço a pagar sendo que o carro custa R$ 60.00 a diária e R$ 0.15 por km rodado
dias = int(input('Por quantos dias o carro foi alugado?'))
km = float(input(' Qual a quantidade de kms percorridos?'))
valortotal = dias * 60.00 + km * 0.15

print(f' O Valor total a pagar pelo aluguel do carro é {valortotal} R$')