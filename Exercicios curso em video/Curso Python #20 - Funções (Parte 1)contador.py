def contador (*núm): # O "*núm" cria tuplas com os números especificados não importa a quantidade - DESEMPACOTAMENTO
    tam = len(núm)
    print(f'Recebi os valores {núm} e são todos {tam} números')



contador(5, 6, 9, 3)
contador(5, 6, 3)
contador(7, 9, 8, 6, 4, 3, 2)
