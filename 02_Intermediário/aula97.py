'''
Modularização: Entendendo os seus próprios módulos python
O primeiro módulo executado se chama __main__
Você pode importar outro módulo inteiro ou parte do módulo
O Python conhece a pasta onde o __main__ está e as
pastas abaixo dele
Ele não reconhece pastas e módulos acima do __main__ por padrão
O Python conhece todos os módulos e pacotes
presentes nos caminhos do sys.path
'''

import aula97_m
from aula97_m import soma, variavel_modulo

# print('Este módulo se chama: ', __name__)
print(aula97_m.variavel_modulo)
print()
print(variavel_modulo)
print()
print(aula97_m.soma(3, 5))
print()
print(soma(4, 5))
print()