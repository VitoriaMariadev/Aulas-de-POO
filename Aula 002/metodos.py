class Carro:
    def __init__(self, nome):
        self.nome = nome

    def acelerar(self):
        print('Alguma coisa')

fusca = Carro('Fusca')

print(fusca.acelerar())