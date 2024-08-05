# Maria pegou um empréstimo de 1.000.000
# para realizar o pagamento em 5 anos.
# A data que ela pegou o emprestimo foi
# 20/12/2020 e o vencimento de cada parcela
# é no dia 20 de cada mês.
# - Crie a data do empréstimo
# - Crie a data do final do empréstimo
# - Mostre todas as datas de vencimento e o valor de cada parcela

from datetime import datetime
from dateutil.relativedelta import relativedelta

valor_emprestimo = 1_000_000

qtd_anos = 5
quantidade_meses_parcelas = qtd_anos * 12

valor_parcela = valor_emprestimo / quantidade_meses_parcelas
numero_parcela = 0
data_emprestimo = datetime(2020, 12, 20)
data_final_emprestimo = data_emprestimo + \
    relativedelta(months=quantidade_meses_parcelas)

datas_parcelas = []
data_parcela = data_emprestimo
    
print(f'Valor do empréstimo: R${valor_emprestimo:,.2f}')
print(f'Quantidade de parcelas: {quantidade_meses_parcelas} meses.')

while data_parcela < data_final_emprestimo:
    data_parcela += relativedelta(months=1)
    datas_parcelas.append(data_parcela)    
    
for data in datas_parcelas:
    numero_parcela += 1    
    print(
        f'Parcela: {numero_parcela}, ' 
        f'Mês: {data_parcela.strftime('%d/%m/%Y')}, '
        f'Valor da Parcela: R${valor_parcela:,.2f}'
    )
