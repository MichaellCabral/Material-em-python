def multiplicador (numero):
        a = 2 # esta variavel tem escopo local
        print(f'dentro da função a variavel "a"vale: {a}')
        return a * numero

a = 3 # esta variavel tem escopo global
b = multiplicador(5)
print(f'fora da função a variavel "a" vale: {a}')