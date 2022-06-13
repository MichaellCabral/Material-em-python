soma_pares = 0 #somar somente numeros pares
cont_pares = 0 # contador de repetição para numeros pares
for numero in range(1,11,1): #usando range como laço de repetição
    if numero %2==0:
        soma_pares = soma_pares + numero
        cont_pares += 1
    else:
        continue # pular a iteração com o for
print(f'A soma acumulada foi {soma_pares} e a quantidade de pares foi  {cont_pares}')
print(f'a média dos numeros pares foi : {soma_pares/cont_pares}')  # soma do pares / total de numeros pares que apareceram