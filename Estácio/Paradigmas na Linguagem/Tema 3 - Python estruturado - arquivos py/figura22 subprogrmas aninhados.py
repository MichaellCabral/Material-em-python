def taximetro(distancia):
    def calculaMult():
        if distancia < 5:
            return 1.2
        else:
            return 1

    multiplicador = calculaMult()
    largada = 3
    km_rodado = 2
    valor = (largada + distancia * km_rodado) * multiplicador
    return valor


dist = eval(input("Entre com a distancia a ser percorrida em km: "))
pagamento = taximetro(dist)
print(f'O valor a pagar é R$ {pagamento}')

#A função taximetro() tem, dentro de sua definição, a definição de outra função denominada calculaMult(). Na linha 7, a função calculaMult() é chamada e o seu retorno é armazenado na variável multiplicador.