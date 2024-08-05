# Valores Truthy e Falsy
# Tipos mutáveis e imutáveis
# Mutáveis [] - List; {} - Dict; () - Set
# Imutáveis () - Tuple; "" - STR; 0 0.0 - Int,Float
# Imutáveis None False range(0, 0) ou vazio.

lista = []
dictionary = {}
Set = set()
Tuple = ()
string = ''
Integer = 0
Float = 0.0
nothing = None
falso = False
interval = range(0)

def falsy(valor):
    return 'falsy' if not valor else 'Truthy'

print(f'Teste', falsy('Teste'))
print(f'{lista=}', falsy(lista))
print(f'{dictionary=}', falsy(dictionary))
print(f'{Set=}', falsy(Set))
print(f'{Tuple=}', falsy(Tuple))
print(f'{string=}', falsy(string))
print(f'{Integer=}', falsy(Integer))
print(f'{Float=}', falsy(Float))
print(f'{nothing=}', falsy(nothing))
print(f'{falso=}', falsy(falso))
print(f'{interval=}', falsy(interval))



