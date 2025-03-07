import conta
import cliente

class Banco:
    def __init__(
        self,
        agencias: list[int] | None = None,
        clientes: list[cliente.Pessoa] | None = None,
        contas: list[conta.Conta] | None = None,
    ):
        self.agencias = agencias or []
        self.clientes = clientes or []
        self.contas = contas or []
    
    def _checa_agencia(self, conta):
        if conta.agencia in self.agencias:
            print('_checa_agencia', True)
            return True
        print('_checa_agencia', False)
        return False
        
    def _checa_cliente(self, cliente):
        if cliente in self.clientes:
            print('_checa_cliente', True)
            return True
        print('_checa_cliente', False)
        return False
        
    def _checa_conta(self, conta):
        if conta in self.contas:
            print('_checa_conta', True)
            return True
        print('_checa_conta', False)
        return False
    
    def _checa_se_conta_e_do_cliente(self, cliente, conta):
        if conta is cliente.conta:
            print('_checa_se_conta_e_do_cliente', True)
            return True
        print('_checa_se_conta_e_do_cliente', False)
        return False

        
    def autenticar(self, cliente: cliente.Pessoa, conta: conta.Conta):
        return self._checa_agencia(conta) and \
            self._checa_cliente(cliente) and \
            self._checa_conta(conta) and \
            self._checa_se_conta_e_do_cliente(cliente, conta)
            
    def __repr__(self) -> str:
        class_name = type(self).__name__
        attrs = f'(Agências:{self.agencias!r}, Clientes:{self.clientes!r}, '\
            f' Contas:{self.contas!r})'
        return f'{class_name}{attrs}'
            
if __name__ == '__main__':
    c1 = cliente.Cliente('Gabriel', 31)
    cc1 = conta.ContaCorrente(111, 222, 0, 0)
    c1.conta = cc1
    c2 = cliente.Cliente('Maria', 25)
    cp1 = conta.ContaPoupanca(333, 444, 0)
    c2.conta = cp1
    
    banco = Banco()
    banco.clientes.extend([c1, c2])
    banco.contas.extend([cc1, cp1])
    banco.agencias.extend([111, 333])
    
    if banco.autenticar(c1, cc1):
        cc1.depositar(10)
        c1.conta.depositar(100)
        print(c1.conta)
    
    # print(banco.autenticar(c1, cp1))
    # print(banco.autenticar(c1, cc1))
    # print(banco.autenticar(c2, cc1))
    # print(banco.autenticar(c2, cp1))
    # print(banco)
    
