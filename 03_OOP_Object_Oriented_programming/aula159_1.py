# dataclasses - O que são dataclasses?
# O módulo dataclasses fornece um decorador e funções para criar métodos como
# __init__(), __repr__(), __eq__() (entre outros) em classes definidas pelo
# usuário.
# Em resumo: dataclasses são syntax sugar para criar classes normais.
# Foi descrito na PEP 557 e adicionado na versão 3.7 do Python.
# doc: https://docs.python.org/3/library/dataclasses.html

from dataclasses import dataclass

@dataclass
class Pessoa:
    nome: str
    idade: int
    
    
if __name__ == '__main__':
    p1 = Pessoa('Gabriel', 31)
    p2 = Pessoa('Gabriel', 31)
    p3 = Pessoa('Maria', 25)
    p4 = Pessoa('Maria', 25)
    print('p1 é igual a p2?', p1 == p2)
    print('p1 é igual a p3?', p1 == p3)
    print('p1 é igual a p4?', p1 == p4)
    print('p2 é igual a p3?', p2 == p3)
    print('p2 é igual a p4?', p2 == p4)
    print('p3 é igual a p4?', p3 == p4)
    
    