class Animal:

    def __init__(self, nome):
        self.nome = nome

    def comendo(self, alimento):
        return f'{self.nome} está comendo {alimento}'
    
    def executar(self, *arg, **kwargs):
        return self.comendo(*arg, **kwargs)
    
leao = Animal(nome='Leão')
print(leao.nome)
print(leao.executar('Maçã'))