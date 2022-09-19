valores = [10, 20, 30]

def altera_lista(lista):
    nova_lista = list(lista)
    nova_lista[2] = nova_lista[2] + 10
    return nova_lista

print("Nova lista", altera_lista(valores))
print("Nova lista", altera_lista(valores))

#No exemplo do script funcao4.py, muito similar ao anterior, ao invés de alterarmos o valor do próprio parâmetro, criamos uma cópia dele (linha 4), sendo assim, não alteramos a variável valores e obtemos o mesmo resultado para as duas chamadas da função (linha 8 e 9).