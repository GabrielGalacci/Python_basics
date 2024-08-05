# namedtuples - tuplas imutáveis com nomes para valores
# Usamos namedtuples para criar classes de objetos que são apenas um
# agrupamento de atributos, como classes normais sem métodos, ou registros de
# bases de dados, etc.
# As namedtuples são imutáveis assim como as tuplas.
# https://docs.python.org/3/library/collections.html#collections.namedtuple
# https://docs.python.org/3/library/typing.html#typing.NamedTuple
# https://brasilescola.uol.com.br/curiosidades/baralho.htm

# maneira 1
# from collections import namedtuple

# Carta = namedtuple(
#     'Carta', ['valor', 'naipe'],
#     defaults=['VALOR', 'NAIPE']
# )

# maneira 2
from typing import NamedTuple

class Carta(NamedTuple):
    valor: str = 'VALOR'
    naipe: str = 'NAIPE'
    

# Aplicação
as_espadas = Carta('A')

print('1', as_espadas._asdict())
print('2', as_espadas)
print('3', as_espadas[0])
print('4', as_espadas.valor)
print('5', as_espadas[1])
print('6', as_espadas.naipe)

print('-------------------')
print('7', as_espadas._fields)
print('8', as_espadas._field_defaults)

print('-------------------')
for valor in as_espadas:
    print(valor)
