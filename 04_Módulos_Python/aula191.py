# pip install requests types-requests
# requests para requisições HTTP
# Utilizar aulas 189 para mais informaçoes e comandos
# a pasta bin dos sistemas unix é scripts em windows

# Tutorial -> https://youtu.be/Qd8JT0bnJGs

import requests

# http:// -> porta 80
# https:// -> porta 443
url = 'http://localhost:3333/'
response = requests.get(url)

print(response.status_code)
print(response.headers)
# print(response.content) # para todos os bits
# print(response.json()) # Para requisição de arquivos json
# print(response.text) # Mostra a escrita HTML

