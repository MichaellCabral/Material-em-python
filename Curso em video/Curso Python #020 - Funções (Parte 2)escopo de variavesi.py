def funcao(b):#programa funcao (ESCOPO LOCAL)
    global a = 7
    b+=4
    c=2
    
    print(f'"a" dentro da funcao local = {a}')
    print(f'"b" dentro da funcao local + 4 = {b}')
    print(f'"c" dentro da funcao local = {c}')
    print('--'*30)

#programa principal (ESCOPO GLOBAL)
a = 10
funcao(a) # pega o valor 5 dessa variavel e joga la no parametro b (5+4=9) cada funcao aparece novamente com a soma b+=4
b = 1
funcao(b)
c = 2
funcao(c)
print(f'"a" dentro do programa global = {a}')
print(f'"b" dentro do programa global = {b}')
print(f'"c" dentro do programa global = {c}')