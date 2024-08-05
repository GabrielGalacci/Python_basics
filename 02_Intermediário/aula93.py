# Try e except para tratar exceções

# a = 18
# b = 0
# c = a / b

try:
    a = 18
    b = 0
    print(b[0])
    # print('Linha 1'[1000])
    c = a / b
    print('Linha 2')
    
except ZeroDivisionError as e:
    print(e.__class__.__name__)
    print(e)

except NameError:
    print('Nome não está definido!')

# Parte 2, tratando mais de 1 except por vez
except (TypeError, IndexError) as e:
    print('TypeError + IndexError')
    print('Nome:', e.__class__.__name__)
    print('Mensagem: ', e)

except Exception:
    print('Erro desconhecido!')

    print('CONTINUAR')