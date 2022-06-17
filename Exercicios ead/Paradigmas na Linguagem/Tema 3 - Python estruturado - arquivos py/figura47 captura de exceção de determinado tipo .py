try:
    num = eval(input("Entre com um número inteiro: "))
    print(num)
except NameError:
    print("Entre com o valor numérico e não letras")

    """Python permite que o bloco relativo ao except só seja executado caso a exceção levantada seja de determinado tipo. Para isso, o except precisa trazer o tipo de exceção que se deseja capturar."""