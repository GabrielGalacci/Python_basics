# Métodos dir, hasattr e getattr em Python
string = 'Gabriel'
method = 'strip'
# method = 'upper'
# method = 'lower'

if hasattr(string, method):
    print(f'Exists {method=}')
    print(getattr(string, method)())
else:
    print('Does not exists method', method)