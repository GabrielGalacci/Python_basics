# Introdução à list comprehension em python
# List comprehension é uma forma rápida para criar listas
# a partir de iteráveis

lista = []
for numero in range(10):
    lista.append(numero)
print(lista)
print()


lista = [
    numero * 2
    for numero in range(10)
]
print(lista)