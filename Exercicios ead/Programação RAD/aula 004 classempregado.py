class empregado:
    'classe base para empregados'
    contador = 0

    def __init__(self,nome,salario):
        self.nome = nome
        self.salario = salario
        empregado.contador += 1

    def mostra_contador (self):
        print("numero de empregados: %d % empregado.contador")

    def mostra_empregado (self):
        print("nome :", self.nome, ",salario: ",self.salario)