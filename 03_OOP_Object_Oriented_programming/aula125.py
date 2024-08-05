# Atributos de classe


class Pessoa:
    ano_atual = 2024  # É um atributo de classe

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nacimento(self):
        return Pessoa.ano_atual - self.idade 
    # Se colocar self no lugar de pessoa pode dar problema
    
p1 = Pessoa('João', 31)
p2 = Pessoa('Maria', 25)

print(Pessoa.ano_atual)

print(p1.get_ano_nacimento())
print(p2.get_ano_nacimento())
