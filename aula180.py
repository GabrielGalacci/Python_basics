# csv.writer e csv.DictWriter para escrever em CSV
# csv.reader lê o CSV em formato de lista
# csv.DictReader lê o CSV em formato de dicionário

import csv
from pathlib import Path

CAMINHO_CSV = Path(__file__).parent / 'aula180.csv'

lista_clientes = [
    {'Nome': 'Gabriel Galacci', 'Endereço': 'Av 1, 22'},
    {'Nome': 'Maria Joaquina', 'Endereço': 'R. 2, "1"'},
    {'Nome': 'Luiz Henrique', 'Endereço': 'Av B, 3A'},
]


# Maneira 1
with open(CAMINHO_CSV, 'w', encoding='utf8') as arquivo:
    nome_colunas = lista_clientes[0].keys()
    escritor = csv.DictWriter(
        arquivo,
        fieldnames=nome_colunas
    )
    escritor.writeheader()

    for cliente in lista_clientes:
        escritor.writerow(cliente)


# Maneira 2
# with open(CAMINHO_CSV, 'w', encoding='utf8') as arquivo:
#     nome_colunas = lista_clientes[0].keys()
#     escritor = csv.writer(arquivo)

#     escritor.writerow(nome_colunas)

#     for cliente in lista_clientes:
#         escritor.writerow(cliente.values())
