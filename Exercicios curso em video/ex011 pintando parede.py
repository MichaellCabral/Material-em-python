larg = float(input('largura da parede: '))
alt = float(input('altura da parede: '))
área = larg * alt
print(f'sua parede tem a dimensao de {larg} x {alt} e sua area é : {área}m²')
tinta = área/2
print(f'Para pintar a parede você precisará de {tinta}L')
#programa que le  a largura e a altura de uma parede em metros. calcule a sua area e a quantidade de tinta necessaria para pinta la, sabendo que cada litro de tinta pinta uma area de 2 metros quadrados.