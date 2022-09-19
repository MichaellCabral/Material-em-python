# Nessa aula, vamos aprender como criar estruturas condicionais aninhadas, usando os comandos if.. elif.. else em programas Python.

# If - para primeira condição
# Elif para as demais condições
# Else para a última condição favorável (não é obrigatório)

nome = str(input('Qual é seu nome?'))
if nome == 'Michaell':
    print('Que nome bonito!')
elif nome == 'Miguel' or nome == 'karla' or nome == 'Solange':
    print('Seu nome é bem popular no Brasil')
elif nome in 'Alexia Larissa Lena':
    print('Belo nome feminino') 
else:
    print('Seu nome é bem normal.')
print(f'Tenha um bom dia, {nome}!')