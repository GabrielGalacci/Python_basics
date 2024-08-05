# + Web Scraping com Python usando requests e bs4 BeautifulSoup
# - Web Scraping é o ato de "raspar a web" buscando informações de forma
# automatizada, com determinada linguagem de programação, para uso posterior.
# - O módulo requests consegue carregar dados da Internet para dentro do seu
# código. Já o bs4.BeautifulSoup é responsável por interpretar os dados HTML
# em formato de objetos Python para facilitar a vida do desenvolvedor.
# - Doc: https://www.crummy.com/software/BeautifulSoup/bs4/doc.ptbr/
# + Instalação
# - pip install requests types-requests bs4

import requests
import re
from bs4 import BeautifulSoup

url = 'http://localhost:3333/'
response = requests.get(url)
raw_html = response.text
bytes_html = response.content
parsed_html_utf8 = BeautifulSoup(
    bytes_html, 'html.parser', from_encoding='utf-8'
)
parsed_html = BeautifulSoup(raw_html, 'html.parser')

# O IF é necessário para poder utilizar title no print
# pois o retorno de title pode ser none
if parsed_html.title is not None:
    print('Title text: ', parsed_html.title.text)
    
top_jobs_heading = parsed_html.select_one('#intro > div > div > article > h2')
top_jobs_heading2 = parsed_html_utf8.select_one('#intro > div > div > article > h2')

# if top_jobs_heading is not None:
#     article = top_jobs_heading.parent
    
#     if article is not None:
#         for p in article.select('p'):
#             print(re.sub(r'\s{1,}', ' ', p.text).strip())

# Com encoding utf-8
if top_jobs_heading2 is not None:
    article2 = top_jobs_heading2.parent
    
    if article2 is not None:
        for p in article2.select('p'):
            print(re.sub(r'\s{1,}', ' ', p.text).strip())
