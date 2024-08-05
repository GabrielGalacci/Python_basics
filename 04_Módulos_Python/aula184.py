# Variáveis de ambiente com Python

# NUNCA MANDE O DOTENV PARA REPOSITÓRIOS PARA NAO TER RISCO DE
# INVASÕES, MUITO IMPORTANTE!!!!!!!

# Para variáveis de ambiente
# Windows PS: $env:VARIAVEL="VALOR" | dir env:
# Linux e Mac: export NOME_VARIAVEL="VALOR" | echo $VARIAVEL
# Para obter o valor das variáveis de ambiente
# os.getenv ou os.environ['VARIAVEL']
# Para configurar variáveis de ambiente
# os.environ['VARIAVEL'] = 'valor'
# Ou usando python-dotenv e o arquivo .env
# pip install python-dotenv
# from dotenv import load_dotenv
# load_dotenv()
# https://pypi.org/project/python-dotenv/
# OBS.: sempre lembre-se de criar um .env-example
# BD_USER="CHANGE-ME"
# BD_PASSWORD="CHANGE-ME"
# BD_PORT=CHANGE-ME
# BD_HOST="CHANGE-ME"

import os

from dotenv import load_dotenv  # type: ignore

load_dotenv()

# print(os.environ) # Mostra todas as variáveis de ambiente
print('BD_USER: ', os.getenv('BD_USER'))
print('BD_PASSWORD: ', os.getenv('BD_PASSWORD'))
print('BD_PORT: ', os.getenv('BD_PORT'))
print('BD_HOST: ', os.getenv('BD_HOST'))
