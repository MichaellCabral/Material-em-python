 # SEMPRE COLOCAR AS VARIÁVEIS DE CONTAGEM E DE USO DO ENUNCIADO NO INICÍO
somaidade = 0  
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for p in range(1,5):
    print(f'-----{p}° PESSOA-----')
    nome = str(input('Nome: ')).strip() # strip para tirar os espaços
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade # somaidade = somaidade + idade (em cada laço)
    if p == 1 and sexo in 'Mm': # se a 1° pessoa for homem "M ou m"
        maioridadehomem = idade # fica com a maior idade digitada
        nomevelho = nome # fica com o nome do mais velho
    if sexo in 'Mm'and idade > maioridadehomem: # se for homem e a idade for maior que o maioridadehomem
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20: # se for mulher menor de 20 anos:
        totmulher20 += 1 # contador para confirmar informação acima de 0-5
    
médiaidade = somaidade / 4  
    
print(f'A média de idade do grupo é de {médiaidade} anos')
print(f'O homem mais velho tem {maioridadehomem} e se chama {nomevelho}')
print(f'Ao todo são {totmulher20} mulheres com menos de 20 anos')



# Exercício Python 056: 
# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. 
# No final do programa, mostre: a média de idade do grupo, 
# qual é o nome do homem mais velho e 
# quantas mulheres têm menos de 20 anos.