def funcao():
    x = 'ola mundo'
    print (x)

x = "teste"
funcao()
print(x)

#Há uma variável fora e dentro da função com o mesmo nome (x). Nesse caso, embora os nomes sejam iguais, o “x” de dentro da função é outra variável, e seu escopo reside na função.

#Já o “x” de fora tem o escopo fora da função. Trata-se de variável diferente, com outro endereço de memória e apenas o mesmo nome da variável interna da função definida na linha 2.