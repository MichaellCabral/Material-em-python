valores = [10, 20, 30]
print('lista original:',valores)

def altera_lista(lista):
    lista[2] = lista[2] + 10
    
    return lista
    

print("Nova lista", altera_lista(valores))
print("Nova lista", altera_lista(valores))