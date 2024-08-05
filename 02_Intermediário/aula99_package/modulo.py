'''
O __all__ indica quais as opções que são entregues
quando a pessoa importa o módulo com import * 
'''
# from modulo_b import fala_oi  # Este modo serve para o modulo.py
# from aula99_package.modulo_b import fala_oi # Este modo serve para o main aula99.py

# __all__ = [
#     'variavel',
#     'soma_do_modulo',
#     'nova_variavel',
# ]

variavel = 'Alguma coisa'

def soma_do_modulo(x, y):
    return x + y

nova_variavel = 'OK'

# fala_oi()
