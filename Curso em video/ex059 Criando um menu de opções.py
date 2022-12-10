from time import sleep
n1 = int(input('Primeiro valor: ')) # primeiro se escolhe os valores
n2 = int(input('Segundo valor: '))
opção = 0
while opção != 5: # enquanto opção for diferente de 5 então:
    print('''    [1] somar 
    [2] multiplicar 
    [3] maior 
    [4] novos números 
    [5] sair do programa''') # dentro de aspas triplas não precisa de indentação
    opção = int(input('>>>>>Qual é a sa opção'))
    
    if opção == 1:
        soma = n1 + n2
        print(f'A soma entre {n1} e {n2} é {soma}')
    elif opção  == 2:
        produto = n1 * n2
        print(f'A multiplicação entre {n1} e {n2} é {produto}')
    elif opção == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f'Entre {n1} e {n2} o maior valor é {maior}')
    elif opção == 4:
        print('Informe os números novamente: ')
        n1 = int(input('Primeiro valor: ')) 
        n2 = int(input('Segundo valor: '))
    elif opção == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente')
    print('=-=' * 10)
    sleep(2)
print('Fim do programa! Volte sempre!')


# Crie um programa que leia dois valores e mostre um menu como o ao lado na tela: 
# Seu programa deverá realizar a operação solicitada em cada caso.
# [1] somar [2] multiplicar [3]  maior [4] novos números [5] sair do programa
