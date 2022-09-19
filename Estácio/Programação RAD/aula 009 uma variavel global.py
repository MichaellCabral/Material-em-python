from re import X


def funcao ():
    global x
    print(x)
    x = 'ola mundo'
    print(x)

x = 'teste'
funcao()
print (x)

#Corrigimos o erro, acrescentando a palavra-chave global na linha 2. Isso indica que o x referido na linha 3 vem de fora da função e é uma variável global.

#Na linha 4, a variável x tem o valor modificado, o qual é levado para fora da função. É possível perceber isso na linha 9: agora, seu valor é “Olá mundo!”, e, antes da chamada, era “Teste”. Em algumas situações, você pode usar esse recurso nos programas.