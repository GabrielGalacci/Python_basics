import sys

'''
Generator Expression, Iterable and Iterators in Python

Generator utiliza os dados em uma lista um por vez, utilizando menos espaço na memória
porém não é possível utilizar a busca ou tratamento da lista, seja com indice ou len

Iteradores guardam todos os dados da lista na memória, gastando uma quantidade infinita
de armazenamento, porém é possível fazer o tratamentos dos dados da lista.
'''

iterable = ['Eu', 'tenho', '__iter__']
iterator = iter(iterable) # possuem __iter__ e __next__

list = [n for n in range(10000)]
generator = (n for n in range(10000))

print(sys.getsizeof(list))
print(sys.getsizeof(generator))

print(generator)

# for n in generator:
#     print(n)