# Exercício - Salve sua classe em JSON

# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.

import json

CAMINHO_ARQUIVO = 'aula127_a.json'

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


p1 = Pessoa('Gabriel', '31')
p2 = Pessoa('João', '21')
p3 = Pessoa('Luiz', '40')
p4 = Pessoa('Maria', '15')

pessoas = [vars(p1), vars(p2), vars(p3), vars(p4)]

def fazer_dump():
    with open(CAMINHO_ARQUIVO, 'w', encoding='utf8') as arquivo:
        print('FAZENDO_DUMP')
        json.dump(
            pessoas,
            arquivo,
            ensure_ascii=False,
            indent=2,
        )

if __name__ == '__main__':
    print('ELE É O __main__')
    fazer_dump()