# utilizando mais de um for em List comprehension

lista = []

# Método 1
for x in range(3):
    for y in range(3):
        lista.append((x, y))
print(lista)
print()

# Método 2
lista = [
    (x, y)
    for x in range(3)
    for y in range(3)
]
print(lista)
print()


lista = [
    [(x, letra) for letra in 'Luiz']
    for x in range(3)
]

print(lista)