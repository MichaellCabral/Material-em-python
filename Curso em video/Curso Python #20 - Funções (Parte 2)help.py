def contador(i, f, p):
    """
    Faz uma contagen e mostra na tela
    i = inicio da contagem
    f = fim da contagem
    p = passo da contagem
    return =  sem retorno
    """    

    c = i
    while c <= f:
        print(f'{c}', end = ' ')
        c += p
    print('FIM!')

contador( 0, 100, 10)