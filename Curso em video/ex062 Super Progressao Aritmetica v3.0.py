# Melhore o EXERCÍCIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos.

# O programa encerra quando ele disser que quer mostrar 0 termos.

print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10 # programa inicia mostrando 10 termos
while mais != 0:
    total = total + mais # váriavel total recebe o valor total + valor digitado pelo usuário
    while cont <= total: # total de elementos que a p.a irá mostrar ao usuário
        print(f'{termo} →', end='')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print(f'Progressão finalizada com {total} termos mostrados')