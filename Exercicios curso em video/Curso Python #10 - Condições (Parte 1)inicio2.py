# Programa mostra a media de duas notas e decide o que mostrar na tela conforme a media final

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda  nota: '))
media = (n1+n2)/2
print(f'A sua nota foi {media:.1f}')

if media >= 6.0:
    print('Sua média foi boa! PARABÊNS!')
else:
    print('A sua média fli ruim! ESTUDE MAIS!')

# CONDIÇÃO SIMPLIFICADA
#print('PARABÊNS' if media >= 6 else 'ESTUDE MAIS!')