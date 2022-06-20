# class
# sintaxe
# Marca, memoria ram, placa de video
class Computador:
    def __init__(self, marca, memoria_ram, placa_video): # o init tem dois underline "__init__"
        self.marca = marca
        self.memoria_ram = memoria_ram
        self.placa_video = placa_video
pass

computador1 = Computador('asus','8gb','nvidia') #colocando dentro do parenteses conforme a ordem fica dinamicamente criado
computador2 = Computador('dell ','10gb','geforce')
computador3 = Computador('acer','16gb','atm')

print(computador1.marca,computador1.memoria_ram,computador1.placa_video)
print(computador2.marca,computador2.memoria_ram,computador2.placa_video)
print(computador3.marca,computador3.memoria_ram,computador3.placa_video)