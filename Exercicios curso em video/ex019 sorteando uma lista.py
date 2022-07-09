import random
aluno1 = str(input('primeiro aluno: '))
aluno2 = str(input('segundo aluno: '))
aluno3 = str(input('terceiro aluno: '))
aluno4 = str(input('quarto aluno: '))
lista = [aluno1,aluno2,aluno3,aluno4]
sorteado = random.choice(lista) # sorteado é uma escolha dentro da lista
print(f'o aluno sorteado foi >>>>>{sorteado}<<<<<<')

#Exercício Python 019: Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.



