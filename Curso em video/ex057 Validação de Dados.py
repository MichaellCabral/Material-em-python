sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0] # strip tira os espaços e .upper() [0] torna maiuscula e faz mostra somente a primeira letra
while sexo not in 'MmFf': # enquanto sexo não está em 'MmFf' então:
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper() # INTERAÇÃO COM USUÁRIO (que deve digitar Mm ou Ff)
print(f'Sexo {sexo} registrado com sucesso')







# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.