nome = str(input('Qual seu nome completo? ')).strip()
print(f'Seu nome tem Silva? {"SILVA" in nome.upper()}')

#Exercício Python 025: Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome, ou seja, em qualquer lugar.
#A resposta mostra verdadeiro ou falso (true or false)

# linha 1 - ".strip" >>> retira os espaços ao redor
# linha 2 - O nome "SILVA" em letras maiusculas retira o erro de alguma letra ser digitada e der falso no final. pois ele transforma todas as letras em maiusculas com o "nome.upper" pra verificar o resultado todo em maisculo
#O "in" nao e um metodo, e sim um operador