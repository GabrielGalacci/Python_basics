"""
Exercício
Exiba os índices da lista
"""
"""
Resolução Professor: 

lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')

indices = range(len(lista))

for indice in indices:
    print(indice, lista[indice], type(lista[indice]))
"""

lista = ['Maria', 'Helena', 'Luiz']

for nome in lista:
    indice = lista.index(nome)
    print(indice, nome, type(nome))