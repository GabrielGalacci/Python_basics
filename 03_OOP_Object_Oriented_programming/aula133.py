# Encapsulamento (modificadores de acesso: public, protected, private)
# Python NÃO TEM modificadores de acesso
# Mas podemos seguir as seguintes convenções
#   (sem underline) = public
#       pode ser usado em qualquer lugar
# _ (um underline) = protected
#       não DEVE ser usado fora da classe
#       ou suas subclasses.
# __ (dois underlines) = private
#       "name mangling" (desfiguração de nomes) em Python
#       _NomeClasse__nome_attr_ou_method
#       só DEVE ser usado na classe em que foi
#       declarado.

from functools import partial


class Foo:
    def __init__(self):
        self.public = 'Isso é Público'
        self.protected = 'Isso é Protegido'
        self.private = 'Isso é Privado'

    def method_public(self):
        print('Método Público!')
        self._method_protected()
        self.__method_private()
        return 'method_public'
        
    def _method_protected(self):
        print('Método Protegido!')
        return '_method_protected'
    
    def __method_private(self):
        print('Método Privado!')
        return '__method_private'
    
f = Foo()
print(f.method_public())