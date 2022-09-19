s = 0
for i in range(5):
    s += 3*i
print(s)

"""
Considere o seguinte trecho de um programa escrito em Python:

  
1 s = 0
2 for i in range(5):
3 s += 3*i
4 print(s)
Assinale a opção que apresenta corretamente o que será impresso na tela. """

"""O laço for vai ser repetido 5 vezes, já que range(5) retorna a sequência (0, 1, 2, 3, 4). Vale observar que a instrução print(s) está fora do laço for, o que a leva a ser executada apenas uma vez quando o laço se encerrar. Isso elimina as opções A e B. A variável s começa com valor zero e é acrescida, a cada iteração, do valor 3*i, sendo que i pertence à sequência (0, 1, 2, 3, 4). Ou seja, s recebe os acréscimos: 0 + 3 + 6 + 9 + 12. Assim, ela termina o laço com o valor 30, que será impresso pela instrução print(s)."""