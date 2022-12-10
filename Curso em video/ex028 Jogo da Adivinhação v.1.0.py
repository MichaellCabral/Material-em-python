from random import randint
from time import sleep

jogador = int(input('Em que número eu pensei? ')) # O jogador tenta adivinhar
print('PROCESSANDO...')# Dá a sensação de que o computador esta pensando
sleep(1) #Espera por 3 segundos

computador = randint(0,5) # Faz o computador "PENSAR"
print('-=-'*20)
print(f'Pensei no número {computador}')
print('-=-'*20)

if jogador == computador:
    print('PARABÊNS! Você conseguiu me vencer!')
else:
    print(f'Ganhei eu pensei no número {computador} e não no número {jogador}')
