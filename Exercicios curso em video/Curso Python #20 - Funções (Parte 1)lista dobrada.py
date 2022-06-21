def dobra (lista):
    print(lista) #mostra os valores da lista
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos += 1
        

valores = [2,3,4,5,6,7,8] 

dobra(valores)
print(valores) # mostra os valores da lista dobrado


