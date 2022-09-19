from datetime import date # aula de módulos aula 08 do primeiro mundo
atual = date.today().year # data atual atribuida a váriavel
nasc = int(input('Ano de nascimento: ')) # data de nascimento do usuário
idade = atual - nasc # idade do usuário 
print(f'Quem nasceu em {nasc} tem {idade} anos em {atual}')
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE')
elif idade < 18:
    saldo = 18 - idade # sendo menor que 18 fica igual ao valor que falta pra 18
    print(f'Você ainda não tem 18 anos. Ainda faltam {saldo} anos para o alistamento') 
    ano = atual + saldo
    print(f'Seu alistamento será em {ano}')
elif idade > 18:
    saldo = idade -18 # sendo maior que 18 fica igual ao valor que passa de 18
    print(f'Você já deveria ter se alistado há {saldo} anos.')
    ano = atual - saldo
    print(f'Seu alistamento foi em {ano}')

# Exercício Python 039: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.