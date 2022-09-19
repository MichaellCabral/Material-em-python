city = input("Digite uma cidade: \n").lower().strip().split() 
print(city)
print(city[0] == "santos")

# Exercício Python 024: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO"
# Linha 1 não precisa do str (sem ele o programa identifica como string)
# o lower transforma a string em maiuscula , o strip tira os espaços antes e depois da strg e o split transforma a string em listas
# Linha 3 pega o primeiro valor da lista e verifica se a palavra santos esta presente independente de maiuscula ou minuscula