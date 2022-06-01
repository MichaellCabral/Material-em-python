norte_lista = ['PA','MA','BA']
print(norte_lista)
sul_lista = ['ES','MG','RJ','SP''PR','SC']
norte_lista.extend(sul_lista)
print(norte_lista) # imprime lista estendida com lista_sul (concatena as duas listas)
print('imprime lista concatenada {}'.format(norte_lista))