'''
Combinations, Permutations e Product - itertools
Combinação - Ordem não importa - iterável + tamanho do grupo
Permutação - Ordem Importa
Produto - Ordem importa e repete valores Únicos
'''

from itertools import combinations, permutations, product

def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()


pessoas = [
    'João', 'Joana', 'Gabriel', 'Letícia'
]

camisetas = [
    ['preta', 'branca'],
    ['p', 'm', 'g'],
    ['masculino', 'feminino', 'unissex'],
    ['algodão', 'poliéster']
]

print('Combinação'.upper())
print_iter(combinations(pessoas, 2))
print('Permutação'.upper())
print_iter(permutations(pessoas, 2))
print('Produto'.upper())
print_iter(product(*camisetas))