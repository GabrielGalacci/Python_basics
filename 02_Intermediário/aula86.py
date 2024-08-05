# Dictionary Comprehension e Set Comprehension

produto = {
    'nome': 'Caneta Azul',
    'preco': '2.5',
    'categoria': 'Escritório',
}

# Dictionary Comprehension
dictionary1 = {
    chave: valor.upper()
    if isinstance(valor, str) else valor
    for chave, valor in produto.items()
    if chave != 'categoria'
    }
print(dictionary1)
print()

# Lista para dict (para isso é necessario que a lista possua 2 atributos, sendo, 1 chave e 1 valor)
lista = [
    ('a', 'valor a'),
    ('b', 'valor b'),
    ('c', 'valor c'),
]

dictionary2 = {
    chave: valor 
    for chave, valor in lista
}
print(dictionary2)
print()

# Set Comprehension
s1 = {2 ** i for i in range(10)}
print(s1)
print()