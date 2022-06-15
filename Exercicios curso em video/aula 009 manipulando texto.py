frase = "curso em video python"
print(frase[9::3])
print(len(frase)) #lens significa comprimento da frase = 14
print(frase.count('o',0,13)) #quantas vezes aparece a letra "o" com fatiamento de "0" ate o "13"
print(frase.find("deo")) # mostra a posicao do "deo" na string
print(frase[::-1]) # mostra a frase do avesso
print(frase.find('android'))  # mostra o "-1" pois a string nao foi encontrada
print('curso' in frase) # mostra se verdadeiro ou falso com operador

# TRANSFORMACAO
frase = frase.replace('python','android') # AQUI CONSEGUE MUDAR PERMANENTEMENTE A PALAVRA DA STRING
print(frase.replace('python', 'android')) #substituiu a palavra python por android
print(frase.upper()) # transforma em maisculo
print(frase.lower()) #transforma em minusculo
print(frase.capitalize()) #somente primeira letra em maiusculo
print(frase.title()) # faz o capitalize palavra por palavra
print(frase.strip()) # remove os espacos do inicio e do fim da string
print(frase.rstrip()) #remove espaco da direita da string
print(frase.lstrip()) #remove espaco da esquerda da string

# DIVISAO
print(frase.split()) # cria uma divisao onde houver espaço e cria uma lista nova
print('-'.join(frase)) #junta a frase  toda 

#ATRIBUINDO NA STRING
frase = frase.split() 
print(frase)
print(frase[0] [2]) # mostra o primeiro item da lista e a letra 2
frase = '-'.join(frase)
print(frase)



