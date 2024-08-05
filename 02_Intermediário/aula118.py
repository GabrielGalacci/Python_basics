'''
Problemas dos parâmetros mutáveis em funções Python
na definição da função abaixo se tivesse lista=[] ocorreria
um problema na hora de executar a função, pois, ela sendo
mutável os valor seriam inseridos a todo tempo, sem
diferenciar as listas
'''

def adiciona_clientes(nome, lista=None):
    if lista is None:
        lista = []
    lista.append(nome)
    return lista

clientes1 = adiciona_clientes('Gabriel')
adiciona_clientes('Luiz', clientes1)
adiciona_clientes('Maria', clientes1)
clientes1.append('Eduardo')

clientes2 = adiciona_clientes('João')
adiciona_clientes('Márcia', clientes2)
adiciona_clientes('José', clientes2)

clientes3 = adiciona_clientes('Jorge')
adiciona_clientes('Cristina', clientes3)
adiciona_clientes('Kléber', clientes3)


print(clientes1)
print(clientes2)
print(clientes3)
