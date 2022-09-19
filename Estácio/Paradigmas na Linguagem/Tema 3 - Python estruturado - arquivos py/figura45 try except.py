try:
    num = eval(input("Entre com um número inteiro: "))
    print(num)
except:
    print("Entre com o valor numérico e não letras")

    """O bloco try é executado primeiro, no qual devem ser inseridas as instruções do fluxo normal do programa.

O bloco except somente será executado se houver o levantamento de alguma exceção."""