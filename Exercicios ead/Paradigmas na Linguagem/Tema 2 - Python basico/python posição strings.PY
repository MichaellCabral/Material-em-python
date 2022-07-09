x = "0123456789 012345"
print(x[0])
print(x[1:3]) # mostra da segunda posição pra frente com tres elementos
print(x[3:]) # mostra da quarta posição pra frente, o espaço vazio mostra tudo
print(x[11:6]) # mostra da posição 11 (depois do espaço e seis elementos)
print(x[:3].join(x[3:]))