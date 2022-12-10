# CONDIÇÃO
# Programa pergunta quantos anos tem seu carro e responde se o carro é novo ou velho conforme a idade do carro
tempo=int(input('Quantos anos tem seu carro? '))

if tempo <=3:
    print('carro novo')
else:
    print('carro velho')
print('--FIM--')

# MODO SIMPIFICADO (Se torna mais complicado por não organizar em blocos)
# print('carro novo'if tempo <=3 else 'carro velho')