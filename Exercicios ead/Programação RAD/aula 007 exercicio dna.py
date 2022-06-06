DNA =  ('a','a','t','c','g','g','g','t','t','a','a','t','g','c','a','a','t','t','c','g')
#programa para contar a quantidade de timinas
t = 0
for i in DNA:
    if  i == 't':
        t = t + 1
print(t)

# programa para contar cada base
t = 0
c = 0
g = 0
a = 0
for i in DNA:
    if i == 'a':
        a=a+1
    elif  i == 't':
        t=t+1
    elif  i == 'c':
        c=c+1
    else:
        g=g+1

print('quantidade de a: {} t:{} c:{} g:{}'.format(a,t,c,g))
