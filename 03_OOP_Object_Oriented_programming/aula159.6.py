# Valores padrão e field em dataclasses

from dataclasses import dataclass, field, fields

@dataclass
class Pessoa:
    nome: str = field(default='Not Sent', repr=False)
    sobrenome: str = 'Not Sent'
    idade: int = 0
    enderecos: list[str] = field(default_factory=list)
    
if __name__ == '__main__':
    p1 = Pessoa()
    # print(fields(p1)) #Fields mostra as definições dos campos da classe
    print(p1)
    