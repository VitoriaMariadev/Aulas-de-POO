class Caneta:
    def __init__(self, cor):
        self._cor = cor # Não deve ser usado

    @property # Não é nescessário colocar o parentese para chamar o metodo
    def cor(self):
        return self._cor
    
    @cor.setter
    def cor(self, valor):
        self._cor = valor

caneta = Caneta('Azul')
caneta.cor = 'Rosa'

print(caneta.cor)