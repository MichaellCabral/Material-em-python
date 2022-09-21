from pessoa import Pessoa
class Pessoa: # Iniciar a classe com letra maiúscula
    p1 = Pessoa # objeto p1 criado a partir da classe Pessoa
    p2 = Pessoa
    p1.nome = 'Michaell' # nome é atributo (variável) de p1
    p2.nome = 'Solange'
    print(p1.nome)