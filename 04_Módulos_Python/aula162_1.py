# Criando datas com módulo datetime
# datetime(ano, mês, dia)
# datetime(ano, mês, dia, horas, minutos, segundos)
# datetime.strptime('DATA', 'FORMATO')
# datetime.now()
# https://pt.wikipedia.org/wiki/Era_Unix
# datetime.fromtimestamp(Unix Timestamp)
# https://docs.python.org/3/library/datetime.html
# Para timezones
# https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
# Instalando o pytz
# pip install pytz types-pytz

from datetime import datetime

data_str_data1 = '2024/02/07 14:16:35'
data_str_fmt1 = '%Y/%m/%d %H:%M:%S'

data_str_data2 = '07/02/2024'
data_str_fmt2 = '%d/%m/%Y'

data1 = datetime.strptime(data_str_data1, data_str_fmt1)
data2 = datetime.strptime(data_str_data2, data_str_fmt2)

print('data 1: ', data1)
print('---')
print('data 2: ', data2)