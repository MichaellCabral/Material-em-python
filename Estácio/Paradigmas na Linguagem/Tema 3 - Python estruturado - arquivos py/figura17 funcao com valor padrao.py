def taximetro(distancia, multiplicador=1):
    largada = 4
    km_rodado = 2
    valor = (largada + distancia * km_rodado) * multiplicador
    return valor


pagamento = taximetro(3.5)
print(pagamento)

"""Atenção
Retornar um valor é diferente de imprimir na tela. Ao utilizar a função print(), ocorre apenas a impressão de algo na tela, o que não significa que tenha havido retorno de qualquer função definida pelo usuário."""