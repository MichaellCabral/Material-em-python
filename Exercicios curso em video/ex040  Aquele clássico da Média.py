nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
média = (nota1 + nota2) /2
print(f'Tirando {nota1:.1f} e tirando {nota2:.1f} a média do aluno é {média:.1f}')

if média >=5 and média < 7:  
    print('O aluno está em recuperação')
elif média < 5:
    print('O aluno está reprovado')
elif média >= 7:
    print('O aluno está aprovado')


# Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# Média abaixo de 5.0: REPROVADO
# Média entre 5.0 e 6.9: RECUPERAÇÃO
# Média 7.0 ou superior: APROVADO