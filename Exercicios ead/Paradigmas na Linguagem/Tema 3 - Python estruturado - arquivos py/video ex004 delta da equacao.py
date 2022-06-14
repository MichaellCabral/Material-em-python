def calculadelta(coef1,coef2,coef3):
    # delta da eq do 2 grau = b^2-4.a.c
    global delta # pra todo mundo enxergar essa variavel delta
    delta = coef2 * coef2 - 4*coef1*coef3
    #return delta ( nao precisa do return com a variavel global)

a = eval(input('entre com o coeficiente a da equacao: '))
b = eval(input('entre com o coeficiente b da equacao: '))
c = eval(input('entre com o coeficiente c da equacao: '))

"""delta = (nao precisa da variavel delta""" 
calculadelta(a,b,c)

print(f'o valor de delta é igual a : {delta}')

#delta > 0 : equacao tem 2 raizes reais
#delta = 0 : equacao tem 1 raiz real
#delta < 0 : equacao nao tem raiz real

if delta>0:
    print('equacao tem 2 raizes reais')
elif delta == 0:
    print('equacao tem 1 raiz real')
else:
    print('equacao nao tem raiz real')