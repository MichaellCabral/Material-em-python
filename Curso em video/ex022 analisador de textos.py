nome = str(input('digite seu nome completo: ')).strip()#strip elimina os espaços antes e depois
print('Analisando seu nome...')
print(f'Seu nome em maiuscula e: {nome.upper()}')
print(f'Seu nome em minuscula e: {nome.lower()}')
print(f'o nome tem {len(nome)-nome.count(" ")} letras') # "-nome.count(" ") conta os espaços e subtrai por eles
print(f'Seu primeiro nome tem  {nome.find(" ")} letras')
#DE OUTRO JEITO PRA VER O NOME E A QUANTIDADE DE LETRAS
separa = nome.split()#separa o nome em uma lista
print(separa)
print(f'Seu primeiro nome e {separa[0]} e ele tem {len(separa[0])} letras')


# Exercicio 022:
# Faça um programa em python que leia o nome completo de uma pessoa e mostre
# mostra o nome com todas as letras maiusculas e minusculas 
# quantas letras ao todo sem considerar espaços 
# quantas letras tem o primeiro nome