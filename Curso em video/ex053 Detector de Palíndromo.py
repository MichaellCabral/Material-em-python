import string


frase = str(input('Digite uma frase: ')).strip().upper() # strip (tira os espaços) upper (maiusculas)
palavras = frase.split() # separa frase em lista
junto = ''.join(palavras) # junta as palavras sem espaço
#inverso = ''  # USADO COM O LAÇO FOR
inverso = junto[::-1] # com este inverso não precisa do FOR
""" #>>>> LAÇO FOR <<<<
for letra in range(len(junto)-1,-1,-1):
    inverso += junto[letra]
"""
print(f'O inverso de {junto} é {inverso}')
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo')


# Exercício Python 053: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.