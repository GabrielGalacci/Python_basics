# Try, except, else e finally (finally sempre será executado!)
# https://docs.python.org/pt-br/3/library/exceptions.html#built-in-exceptions

'''
Sempre utilizar o except com as exceções separadamente para ter mais
controle sobre os erros que podem acontecer no código!!!!!!
'''

try:
    print('ABRIR ARQUIVO!')
    # 8/0
    # b

except ZeroDivisionError as e:
    print(e.__class__.__name__)
    print(e)
    print('DIVIDIU POR ZERO!')

except IndexError as error:
    print('IndexError')

except (NameError, ImportError): # erros aninhados
    print('NameError, ImportError')

else:
    print('Não ocorreu nenhum erro!')

finally:
    print('FECHAR ARQUIVO!!!')