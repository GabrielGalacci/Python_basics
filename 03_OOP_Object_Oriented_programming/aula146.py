# Criando Exceptions em Python Orientado a Objetos
# Para criar uma Exception em Python, você só
# precisa herdar de alguma exceção da linguagem.
# A recomendação da doc é herdar de Exception.
# https://docs.python.org/3/library/exceptions.html
# Criando exceções (comum colocar Error ao final)
# Levantando (raise) / Lançando (throw) exceções
# Relançando exceções
# Adicionando notas em exceções (3.11.0)
# Levantando e tratando suas Exceptions (Exceções)
# Notas das exceptions em Python (add_notes, __notes__)
class MyError(Exception):
    ...


class AnotherError(Exception):
    ...

def raise_error():
    exception_ = MyError('My error Message')
    exception_.add_note('Nota 1')
    exception_.add_note('Você errou isso')
    raise exception_

try:
    raise_error()
except MyError as error:
    print(error.__class__.__name__)
    print(error.args)
    print(error)
    print()
    exception_ = AnotherError('Vou lançar de novo')
    exception_.__notes__ = error.__notes__.copy()
    exception_.add_note('Mais uma nota')
    raise exception_ from error
