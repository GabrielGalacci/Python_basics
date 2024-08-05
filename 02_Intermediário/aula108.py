'''
Count é um iterador sem fim (itertools)
CUIDADO PARA NÃO STARTAR O COUNT SEM TER UM FIM.
'''

from itertools import count

c1 = count(step=8, start=0)
r1 = range(0, 100, 8)

print('c1', hasattr(c1, '__iter__'))
print('c1', hasattr(c1, '__next__'))
print('r1', hasattr(r1, '__iter__'))
print('r1', hasattr(r1, '__next__'))
print()

print('COUNT')
for i in c1:
    if i >= 100:
        break

    print(i)

print()

print('RANGE')
for i in r1:
    print(i)