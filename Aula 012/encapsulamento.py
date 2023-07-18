class Foo:
    def __init__(self):
        self.public = 'Isso é público'
        self._protected = 'Isso é protegido' # Um '_' significa que é protegido e deve ser usado apenas dentro da classe ou de suas subclasses
        self.__private = 'Isso é privado' # Dois '__' significa que é privado e deve ser usado apenas dentro da sua classe

    def __metodo_private(self):
        return '__metodo_private'

a = Foo()

# print(a.__metodo_private()) # Não é possível acessar desta forma.