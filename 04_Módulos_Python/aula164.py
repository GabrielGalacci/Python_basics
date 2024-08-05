# Formatando datas do datetime
# datetime.strftime('DATA', 'FORMATO') Retorna uma string
# Impossibilitando calculo.
# https://docs.python.org/3/library/datetime.html

from datetime import datetime

data = datetime.strptime('2024-02-08 12:25:50', '%Y-%m-%d %H:%M:%S')
print('1', data.strftime('%d/%m/%Y'))
print('2', data.strftime('%d/%m/%Y %H:%M'))
print('3', data.strftime('%d/%m/%Y %H:%M:%S'))
print('ANO:', data.strftime('%Y'), data.year)
print('DIA:', data.strftime('%d'), data.day)
print('MÊS:', data.strftime('%m'), data.month)
print('HORA:', data.strftime('%H'), data.hour)
print('MINUTO:', data.strftime('%M'), data.minute)
print('SEGUNDO:', data.strftime('%S'), data.second)
