'''
Considerando duas listas de inteiros ou float(lista a e lista b)
some os valores nas listas, retornando o valor somado em uma nova lista:

Se uma lista for maior que a outra, a soma só vai considerar
o tamanho da lista menor
'''

l1 = [1, 2, 3, 4, 5, 6]
l2 = [1, 2, 3, 4]

'''Solução 1'''

def zipper(l1, l2):
    intervalo = min(len(l1), len(l2))
    return [(l1[i] + l2[i]) for i in range(intervalo)]

print(zipper(l1, l2))

'''Em list Comprehension'''

# lista_soma = [x + y for x, y in zip(l1, l2)]
# print(lista_soma)

'''Outras soluções'''

# lista_soma = []
# for i in range(len(l2)):
#     lista_soma.append(l1[i] + l2[i])
# print(lista_soma)

# lista_soma = []
# for i, _ in enumerate(l2):
#     lista_soma.append(l1[i] + l2[i])
# print(lista_soma)

'''Somando todos os valores, inclusive da lista maior'''
from itertools import zip_longest

lista_soma = [x + y for x, y in zip_longest(l1, l2, fillvalue=0)]
print(lista_soma)
