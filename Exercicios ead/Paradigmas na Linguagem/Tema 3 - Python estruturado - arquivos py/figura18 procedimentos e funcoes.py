def func1(x):
    x = 10
    print(f'Função func1 - x = {x}')


def func2(x):
    x = 20
    print(f'Função func2 - x = {x}')


x = 0
func1(x)
func2(x)
print(f'Programa principal - x = {x}')
<<<<<<< HEAD
=======


#As funções func1(x) e func2(x) não possuem qualquer retorno. Ou seja, são funções com comportamento de procedimentos.

"""
As linhas 1, 2 e 3 definem a função func1(x), que recebe o parâmetro x, mas tem uma variável local de nome x, cujo valor atribuído é 10;
Analogamente, a função func2(x) – definida nas linhas 6, 7 e 8 – que recebe o parâmetro x e tem uma variável de mesmo nome, mas com valor atribuído 20;
O programa principal tem uma variável global de mesmo nome x, cujo valor atribuído é 0, na linha 11;
Veja que as chamadas às funções func1(x) e func2(x) ocorrem nas linhas 12 e 13, quando a variável x global já recebeu o valor 0. Porém, ao serem executadas, cada uma dessas funções tem a sua própria variável local, a quem todas as referências internas são feitas."""
>>>>>>> 56be21461d9ccc761292a7b14f4a72e4b127bec0
