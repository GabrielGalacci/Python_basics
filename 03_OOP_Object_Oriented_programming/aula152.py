# Funções decoradoras e decoradores com classes

def my_repr(self):
    class_name = self.__class__.__name__
    class_dict = self.__dict__
    class_repr = f'{class_name}{class_dict}'
    return class_repr

def add_repr(cls):
    cls.__repr__ = my_repr
    return cls

def my_planet(method):
    def inside(self, *args, **kwargs):
        result = method(self, *args, **kwargs)

        if 'Earth' in result:
            return "You're home!"
        return result
    return inside



@add_repr
class Team:
    def __init__(self, name):
        self.name = name


@add_repr
class Planet:
    def __init__(self, name):
        self.name = name

    @my_planet
    def show_name(self):
        return f'The Planet is: {self.name}'

brasil = Team('Brasil')
portugal = Team('Portugal')

earth = Planet('Earth')
mars = Planet('Mars')

print(brasil)
print(portugal)

print(earth)
print(mars)

print(earth.show_name())
print(mars.show_name())
