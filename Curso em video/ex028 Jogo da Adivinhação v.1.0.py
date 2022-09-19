from random import randint
from time import sleep
computador = randint(0,5) # Faz o computador "PENSAR"
print('-=-'*20)
print(f'Pensei no número {computador}')
print('-=-'*20)
jogador = int(input('Em que número eu pensei? ')) # O jogador tenta adivinhar
print('PROCESSANDO...')# Dá a sensação de que o computador esta pensando
sleep(3) #Espera por 3 segundos
if jogador == computador:
    print('PARABÊNS! Você conseguiu me vencer!')
else:
    print(f'Ganhei eu pensei no número {computador} e não no número {jogador}')
