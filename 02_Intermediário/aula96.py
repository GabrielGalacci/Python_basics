'''
Módulos padrão do Python(import, from, as e *)
https://docs.python.org/3/py-modindex.html
'''

'''
inteiro - import nome_modulo
Vantagens: Você tem o namespace do módulo
Desvantagens: Nomes muito grandes

por ter o namespace do módulo as suas variáveis 
não atrapalham os nomes dos módulos
'''

# import sys

# platform = 'A minha'
# print(sys.platform)
# print(platform)
# sys.exit()

'''
Partes dos módulos - from nome_modulo import objeto1, objeto2
Vantagens: Nomes pequenos
Desvantagens: Sem o Namespace do módulo
'''

# from sys import exit, platform

# platform = 'A minha' # a variável atrapalha a chamado do módulo
# print(platform)

'''
Alias, forma 1 - cria um apelido para o módulo a ser utilizado
import nome_modulo as apelido
'''

# import sys as s

# sys = 'alguma coisa' # com o alias é possível utilizar o nome para variáveis
# print(s.platform)
# print(sys)

'''
alias, forma 2 - cria um apelido para todas as ferramentas utilizadas do módulo
from nome_modulo import objeto as apelido
'''

# from sys import exit as ex, platform as pf

# print(pf)

'''
Vantagens: Você pode reservar nomes para seu código
Desvantagens: Pode ficar for do padrão da linguagem
'''

'''
Má práica, pegar todos os objetos do módulo
from nome_modulo import *

Vantagens: Importa tudo do módulo
Desvantagens: Importa de fato TUDO do módulo
'''

# from sys import *

# print(platform)
# exit()


