n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()
print(f'Muito prazer em te conhecer!')
print(f'Seu primeiro nome é : {nome[0]}')
print(f'Seu último nome é {nome[len(nome)-1]}')

# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

# Linha 2 >>> seu nome completo na variavel "n" entra na variavel "nome" como uma lista ".split()"
# Linha 5 >>> "len serve pra ver quantas posições tem na lista "nome"