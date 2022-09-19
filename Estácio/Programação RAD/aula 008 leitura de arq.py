a = open('c:\\Users\\Adoradores\\desktop\\exemplo.txt')
for linha in a:
    print(linha) #mostra o conteudo do arquivo linha a linha

#ler todas as linhas de um arquivo
conteudo = a.read()
print(conteudo)

#ler o conteudo em lista
lista = a.readlines()
print(lista)

#ler o arquivo linha por linha
lin1 = a.readline()
lin2 = a.readline()
print(lin1,lin2)
"""
#criando um novo arquivo colocando "w" no final (0 kb )
b = open('c:\\Users\\Adoradores\\desktop\\novoarquivo','w')
#Verifique na pasta de seu computador que, agora, há um novo arquivo com o tamanho 0 kb (vazio).
b.write("escrevendo no novo arquivo de texto")

for linha in b:
    print(linha) NAO FUNCIONOU VOU VERIFICAR
"""
dados = a .readlines()
print (dados)
dados.append("nova linha inserida no arquivo")
a.writelines(dados) 
print(dados)
#O método writelines() é diferente do write() porque aceita uma lista de strings, enquanto o write aceita uma string apenas.