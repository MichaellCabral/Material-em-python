from this import s
def  soma (* valores): # O asterisco é o simbolo de DESEMPACOTAMENTO
    s = 0
    for num in valores:
        s += num
    
    print(f'somando os valores{valores} temos {s}')
    

soma(2, 2, 2, 2)
soma(1, 1, 1, 1, 1, 1, 1)
soma(3, 3, 3)    