valor = 20

def multiplica(fator):
    global valor
    valor = valor * fator
    print(f'Resultado {valor}')

multiplica(3)
multiplica(3)

"""funcao1.py, definimos uma função chamada multiplica, que multiplica a variável global valor por um fator passado como parâmetro. O valor do resultado é atribuído à variável valor novamente (linha 5), que é impresso em seguida (linha 6).

Ao chamarmos a função multiplica(3) pela primeira vez (linha 8), obtemos a saída “Resultado 60”. Como modificamos a própria variável global valor no corpo da função, ao chamarmos novamente a função multiplica(3) (linha 9), obtemos um resultado diferente para a saída: “Resultado 180”.

Além de não depender apenas dos parâmetros, essa função não retorna valor algum. A função multiplica deste script não é pura."""