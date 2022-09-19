velocidade = float(input('Qual é a velocidade atual do carro? '))
if velocidade >= 80:
    print('MULTADO! Você excedeu o limite permitido que é de 80 km/h')
    multa = (velocidade - 80) * 7
    print(f'Você deve pagar uma multa de {multa:.2f}')
print('Bom dia! Dirija com segurança')

# Exercício Python 029: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
# LINHA 2 >>> Se velocidade for maior ou igual a 80
# LINHA 3 >>> Mostrar na tela que o motorista foi multado
# LINHA 4 >>> calcula o valor da multa ( velocidade - 80 que é o limite) vezes 7 que é o valor da multa
# LINHA 5 >>> Mostra na tela o valor da multa a pagar
# A condição não tem o "else" = "Princípio de condição simples"