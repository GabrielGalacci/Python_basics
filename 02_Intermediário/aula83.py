# Empacotamento e desempacotamento de dicionários
a, b = 1, 2
a, b = b, a
print(a, b)
print()

pessoa = {
    'Nome': 'Gabriel',
    'Sobrenome': 'Galacci',
}


(a1, a2), (b1, b2) = pessoa.items()
print(a1, a2)
print(b1, b2)
print()

pessoa = {
    'Nome': 'Aline',
    'Sobrenome': 'Souza',
}

dados_pessoa = {
    'Idade': 16,
    'Altura': 1.6,
}

pessoa_completa = {**pessoa, **dados_pessoa}
print(pessoa_completa)
print()


# args e kwargs
# args (argumentos não nomeados!)
# kwargs (keyword argumentos - argumentos nomeados)

def mostro_argumentos_nomeados(*args, **kwargs):
    print('NÃO NOMEADOS: ', args)
    print()

    for chave, valor in kwargs.items():
        print(chave, valor)
    print()

mostro_argumentos_nomeados(**pessoa_completa)

configuracoes = {
    'arg1': 1,
    'arg2': 2,
    'arg3': 3,
    'arg4': 4,
}
mostro_argumentos_nomeados(**configuracoes)