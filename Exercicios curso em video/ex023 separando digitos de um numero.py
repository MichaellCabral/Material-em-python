# Faça um programa que leia um mumero de 0 a 9999 e mostre na tela cada um dos digitos separados

num = int(input('Informe um numero: '))
u = num // 1 % 10 #dividir o numero inteiro por 1 e tira o modulo de 10 (resto da divisao)
d = num // 10 % 10 #na dezena divide por 10 e pega o resto
c = num // 100 % 10 
m = num // 1000 % 10
print(f'Analisando o numero {num}')
print(f'unidade: {u}') # na posicao 3 esta a unidade
print(f'dezena:  {d}') # na posicao 2 esta a dezena
print(f'centena: {c}') # na posicao 1 esta a centena
print(f'milhar : {m}') # na posiçao zero esta o milhar