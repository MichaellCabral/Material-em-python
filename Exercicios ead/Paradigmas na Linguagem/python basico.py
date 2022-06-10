x = 'ola mundo'
print(f'x equivale a {x}')

#a letra f  pra colocar a variavel entre chaves pois fica mais organizado

idade = eval(input(f'entre com o valor da sua idade: '))
idade += 10
print(f'Este é o tipo da variavel{(type(idade))}') # veja que com o ficou visualmente melhor
print('Este é o tipo da variavel{}'.format(type(idade))) # veja o mesmo print sem o f
print(f'a idade + 10 vale: {idade}')
print('a idade + 10 vale: {}'.format(idade))