frase = str(input('Digite uma frase: ')).upper() .strip()
print(f'A letra A aparece {frase.count("A")} vezes na frase: ')
print(f'A primeira letra "A" apareceu na posição {frase.find("A")+1}')
print(f'A ultima letra "A" esta na posição {frase.rfind("A")+1}')

# Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

 
# ATENÇÃO: na linha 5 a letra "A" tem de estar entre aspas duplas
# Linha 4 >>> A str (string é importante para usar o ".upper" da str, pois transforma a frase em maiúscula e conta todas as letras maiúscula na string)
# Linha 4 >>> ".strip" Elimina os espaços fora do texto principal
# Linha 6 >>> +1 porque os elementos se contam a partir da posição "0"
# Linha 7 >>> rfind (right find) conta da direita pra esquerda até encontrar a letra "A"