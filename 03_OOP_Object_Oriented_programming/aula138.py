# Herança simples - Relações entre classes
# Associação - usa, Agregação - tem
# Composição - É dono de, Herança - É um
#
# Herança vs Composição
#
# Classe principal (Pessoa)
#   -> super class, base class, parent class
# Classes filhas (Cliente)
#   -> sub class, child class, derived class

class Pessoa:
    cpf = "123456"

    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def falar_nome_classe(self):
        print('Classe Pessoa')
        print(self.nome, self.sobrenome, self.__class__.__name__)


class Cliente(Pessoa):
    def falar_nome_classe(self):
        print('Classe Cliente')
        print(self.nome, self.sobrenome, self.__class__.__name__)

    
class Aluno(Pessoa):
    cpf = 'CPF Aluno'


c1 = Cliente('Gabriel', 'Galacci')
c1.falar_nome_classe()
a1 = Aluno('José', 'Silva')
a1.falar_nome_classe()
print(a1.cpf)
# help(Cliente)
        