distancia = float(input('Qual a distancia da sua viagem? '))
print(f'Você esta prestes a comecar uma viagem de {distancia} km')

if distancia <= 200:
    preço = distancia * 0.50
else:
    preço = distancia * 0.45
print('O preço da sua passagem será de R$ {preço:.2f}')

# Exercício Python 031: Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
# LINHA 4 >>> A condição verifica o preço multiplicado pela distancia percorrida, se menor que 200 km é cobrado o valor de 0.50 por km senão o preço cobrado é de 0.45 centavos por km