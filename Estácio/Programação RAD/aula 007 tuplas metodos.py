minha_tupla1 = ('m','i','c','h','a','e','l','l')
print(len(minha_tupla1)) #qnts elementos tem na tupla

minha_tupla2 = ('brito','cabral') #concatenar tuplas
unir = minha_tupla1 + minha_tupla2
print(unir)

repetir_tupla = ('mi' ,) # Repetir tupla note o detalhe da virgula
print(repetir_tupla*10)

minha_tupla1
print('c' in minha_tupla1) #verifica se "c" pertence a tupla

for i in minha_tupla1: #foreach. iterar sobre listas, arrays e tuplas
    print(i)