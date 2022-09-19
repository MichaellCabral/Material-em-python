valor = 20

def multiplica(valor, fator):
    valor = valor * fator
    return valor

print(f'Resultado, {multiplica(valor, 3)}')
print(f'Resultado, {multiplica(valor, 3)}')

"""funcao2.py, utilizamos a variável valor como mais um parâmetro para a função multiplica. As duas vezes que executamos essa função (linha 7 e 8), elas retornam o mesmo valor, 60.

A função multiplica deste script é um exemplo de função pura, pois depende apenas de seus parâmetros para gerar o resultado, e não acessa ou modifica nenhuma variável externa à função e retorna um valor."""