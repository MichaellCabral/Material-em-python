peso = input ('digite o seu peso em kg: ')
altura = input ('digite a sua altura em metros: ')
imc = float(peso)/(float(altura)*float(altura))
if imc <= 17:
    print ('muito abaixo do peso')
elif imc > 17 and imc < 18.5:
    print ('abaixo do peso')
elif imc >18.5 and imc < 25:
    print ('peso normal')
elif imc > 25 and imc < 30:
    print ('acima do peso')
elif imc > 30 and imc < 35:
    print ('obesidade I')
elif imc > 35 and imc < 40:
    print (' obesidade severa II')
else:
    print ("obesidade III mórbida")
