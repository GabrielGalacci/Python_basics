# datetime.timedelta e dateutil.relativetimedelta (calculando datas)
# Docs:
# https://dateutil.readthedocs.io/en/stable/relativedelta.html
# https://docs.python.org/3/library/datetime.html#timedelta-objects

from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

fmt = '%d/%m/%Y %H:%M:%S'
data_inicio = datetime.strptime('20/04/1987 09:30:30', fmt)
data_fim = datetime.strptime('12/12/2022 08:20:20', fmt)
delta1 = timedelta(days=10, hours=2)
print('1:', data_fim - delta1)
print('2:', data_fim)
print('3:', delta1.days, delta1.seconds)
print('4:', delta1.total_seconds())
print('5:', data_fim > data_inicio)
print('6:', data_fim < data_inicio)
print('7:', data_fim == data_inicio)

delta2 = relativedelta(data_fim, data_inicio)
print('8:', delta2.days, delta2.years)
print('9:', data_fim + relativedelta(seconds=60, minutes=10))
