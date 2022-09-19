def somar(a=0, b=0, c=0): # "a, b e c" são parametros opcionais pois receberam valor "0".
    s = a + b + c
    print(f'A soma é igual a: {s}')

somar(3, 2 ,5)
somar(3, 2)
somar()