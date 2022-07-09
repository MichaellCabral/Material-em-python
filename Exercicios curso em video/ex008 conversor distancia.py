medida = float(input('digite uma distancia em metros: '))
cm = medida * 100
mm = medida * 1000
print ('A medida de {}\n em centimetros é {:.0f} \n em milimetros é {:.0f}'.format(medida,cm,mm))
# Programa conversor de unidade de metros pra centimetros e milimetros
# Dentro das chaves do resultado esta "{:.0f} pra mostrar sem ponto flutuante"