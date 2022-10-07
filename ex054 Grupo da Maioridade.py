from datetime import date # trabalhar com data
atual = date.today().year # trabalhar com o ano atual
totmaior = 0
totmenor = 0
for pessoa in range(1,8):
    nasc = int(input(f'Em que ano a {pessoa}° pessoa nasceu? ')) # pessoa funciona como contador
    idade =  atual - nasc # idade atual
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print(f'Ao todo tivemos {totmaior} pessoas maiores de idade') 
print(f'E também tivemos {totmenor} pessoas menores de idade')

# Exercício Python 054: Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.