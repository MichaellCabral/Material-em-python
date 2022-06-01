estados = ['SP','RJ','ES']
print(estados) # imprime a lista de estados
estados.append('PA') # com a inserçao do "PA"
print(estados) 
estados.pop(2) # remoçao da posicao 2 = "ES"
print(estados) 
estados.remove('PA') # remoçao qnd nao se sabe a posicao, se usa o nome
print(estados)
estados.insert(1,'GO') # objeto inserido na posicao "1"
print(estados)
estados.sort() # sort para ordem crescente
print('ordem crescente {}'.format(estados))
import random # importar biblioteca random
random.shuffle(estados) # bagunçar a lista
print('embaralhados    {}'.format(estados))
estados.reverse()
print('ordem reversa   {}'.format(estados))
estados.append('MG')
estados.append('MG') # inseri duas vezes Minas Gerais
print(estados)
print('qnts vezes vem descrito "MG" = {}'.format(estados.count('MG')))
print(estados)
estados.index('GO') #retorna a posicao do objeto no indice
print('posicao "{}" do objeto Goias no indice'.format(estados.index('GO'))) 
# imprime na tela a posicao do objeto no indice com a importacao random