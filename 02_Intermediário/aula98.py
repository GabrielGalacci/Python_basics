''' 
os módulos python são utilizados no modo singleton, ou seja,
eles são obtidos apenas uma vez.
Para que ele seja obtido mais de uma vez na instância executada
é necessário utilizar o módulo importlib
'''

import importlib

import aula98_m

print(aula98_m.variavel)

for i in range(10):
    importlib.reload(aula98_m)
    print(i)

print('Fim')