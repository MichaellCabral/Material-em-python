def func1():
    global x
    x = 10
    print(f'Função func1 - x = {x}')


def func2():
    global x
    x = 20
    print(f'Função func2 - x = {x}')


x = 0
func1()
func2()
print(f'Programa principal - x = {x}')
<<<<<<< HEAD
=======

#Percebe-se que o print() do programa principal está na linha 16, depois da chamada à função func2(x). Dessa forma, a variável global x foi alterada na execução da func2(x) e fica com o valor 20 quando a execução volta ao programa principal.
>>>>>>> 56be21461d9ccc761292a7b14f4a72e4b127bec0
