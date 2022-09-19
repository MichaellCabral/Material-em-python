strg1 =  'nabucodonosor'
print(strg1)
print(strg1[0])
print(strg1[1])
#trings são imutáveis quanto à alteração por índice
# strg1[0] = "f" (nao altera)

#iterar com comando for
for i in strg1:
    print(i)

#fatiar (slice)
print(strg1[0:5])
print(strg1[5:])
print(strg1[-1])
print(strg1[:])

#verificar se um caracter esta na string
print('f' in strg1)
print('n' in strg1)
#tamanho da string
print(len(strg1))

#conversao de maiuscula ou minusculas
print(strg1.upper())
print(strg1.lower())

"""conversao numero pra string NAO FUNCIONA ESTOU VERIFICANDO
x = 666
type(x)
<class 'int'>
x1 = str(x)
type(x1)
print(class 'strg')
"""

print("-".join(strg1)) #metodo nao altera a string

strg2 = " aquarela do Brasil "
print(strg2.strip())# tira os espaços da borda
