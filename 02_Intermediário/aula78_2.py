# Sets são eficientes para remover valores duplicados
# de iteráveis.
# - Seus valores serão sempre únicos;
# - Não aceitam valores mutáveis;
# - não tem índexes;
# - não garantem ordem;
# - são iteráveis (for, in, not in)

l1 = [1, 2, 3, 3, 3, 3, 3, 1]
s1 = set(l1)
l2 = list(s1)
print(f'{l1=}')
print()
print(f'{s1=}')
print()
print(f'{l2=}')
print()

s1 = {1, 2, 3}
print(f'{s1=}')

print(3 not in s1)
print()

for numero in s1:
    print(numero)

print()    