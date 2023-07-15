class Caneta:
    def __init__(self, cor):
        self.cor_tinta = cor #proteção para caso o nome da váriavel seja modificado

    @property # Não é nescessário colocar o parentese para chamar o metodo
    def cor(self):
        return self.cor_tinta

caneta = Caneta('Azul')

print(caneta.cor)

################ OUTRA FORMA ###########################

# class Caneta:
#     def __init__(self, cor):
#         self.cor = cor #proteção para caso o nome da váriavel seja modificado

#     def get_cor(self):
#         return self.cor

# caneta = Caneta('Azul')

# print(caneta.get_cor())