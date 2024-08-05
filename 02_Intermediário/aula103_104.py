'''
Funções decoradoras
Decorar = Adicionar / Remover / Restringir / Alterar
Funções decoradoras são funções que decoram outras funções
'''

def criar_funcao(func):

    def interna(*args, **kwargs):
        print('Vou te decorar!')
        for arg in args:
            e_string(arg)
        resultado = func(*args, **kwargs)
        print(f'O seu resultado foi {resultado}.')
        print('OK, agora você foi decorada!')
        return resultado
    return interna

'''
Decoradores são usados para fazer o Python
usar as funções decoradoras em outras funções.
Decoradores são "Syntax Sugar" (@ - Açúcar sintático)
'''

@criar_funcao
def inverte_string(string):
    print(inverte_string.__name__)
    return string[::-1]

def e_string(param):
    if not isinstance(param, str):
        raise TypeError('param deve ser uma string!')
    


invertida = inverte_string('123')
print(invertida)