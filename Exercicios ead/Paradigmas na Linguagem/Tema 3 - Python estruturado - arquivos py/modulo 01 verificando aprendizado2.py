s = 0
a = 1
while s < 5:
    s = 3*a
    a += 1
    print(s)

"""Ao ser testada pela primeira vez, a condição do while é verdadeira, já que s vale zero. Assim, a variável s recebe o valor 3 (3x1) e a variável a é acrescida de uma unidade, ficando com o valor 2. Em seguida, é impresso o valor de s (3). A condição do while é, então, testada novamente, sendo mais uma vez verdadeira, porque s tem o valor 3 (menor que 5). Nessa iteração, a variável s recebe o valor 6 (3x2) e a variável a é acrescida de uma unidade, ficando com o valor 3. Em seguida, é impresso o valor de s (6). A condição do while é, então, testada novamente e é falsa, já que s tem o valor 6, maior que 5. Com isso, o laço while é encerrado e nada mais é impresso. Logo, foram impressos os valores 3 e 6."""  