import conta

class Pessoa():
    def __init__(self, nome: str, idade: int) -> None:
        self._nome = nome
        self._idade = idade

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, nome: str):
        self._nome = nome

    @property
    def idade(self):
        return self._idade
    
    @idade.setter
    def idade(self, idade: int):
        self._idade = idade

    def __repr__(self) -> str:
        class_name = type(self).__name__
        attrs = f'({self.nome!r}, {self.idade!r})'
        return f'{class_name}{attrs}'

class Cliente(Pessoa):
    def __init__(self, nome: str, idade: int) -> None:
        super().__init__(nome, idade)
        self.conta: conta.Conta | None = None
        
        

if __name__ == '__main__':
    c1 = Cliente('Gabriel', 31)
    c1.conta = conta.ContaCorrente(111, 222, 0, 0)
    print(c1)
    print(c1.conta)
    print()
    c2 = Cliente('João', 25)
    c2.conta = conta.ContaCorrente(333, 444, 100, 100)
    print(c2)
    print(c2.conta)
    print()
    c3 = Cliente('Maria', 25)
    c3.conta = conta.ContaPoupanca(555, 666, 100)
    print(c3)
    print(c3.conta)
