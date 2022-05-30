 # Ordem de precedência
 #1 ()
 #2 **
 #3 */ // %
 #4 + -
a=5+2*3
b=5*2
c=19/2
d=19//2 
e=122%3
f=4**3
g=pow(4,3)
h=81**(1/2) #raiz quadrada de 81
i=25**(1/2) #raiz quadrada de 25
j=125**(1/3) #raiz cubica de 125
print(a,b,c,d,e,f,g,h,i,j)
x=print('=='*20)
n1 = int(input('digite um valor: '))
n2 = int(input('outro valor: '))
s = n1+n2
m = n1 * n2
d = n1 / n2
di = n1//n2
e = n1 ** n2
print('a soma é{}, \n o produto é {} \n a divisão é {:3f}'.format(s,m,d), end='>>>')
print('divisao inteira {} e potencia {}'.format(di,e))