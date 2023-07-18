"""
Classe Pessoa: Crie uma classe que modele uma pessoa:

Atributos: nome, idade, peso e altura
Métodos: Envelhercer, engordar, emagrecer, crescer. Obs: Por padrão, a 
cada ano que nossa pessoa envelhece, sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.
"""

class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self, anos):
        try:
            if anos <= 0:
                print('--- Valor inválido ---')
            else:
                    self.idade += anos

                    if self.idade >= 21:
                         self.altura += (anos*0.005)
        except:
            print('--- Não foi possível realizar a ação ---')

    def engordar(self, peso):
        try:

            if peso <= 0:
                print('--- Valor inválido ---')
            self.peso += peso
        
        except:
             print('--- Não foi possível realizar ação ---')

    def emagrecer(self, peso):
        try:
            if peso <= 0:
                print('--- Valor inválido ---')
            self.peso -= peso
        
        except:
             print('--- Não foi possível realizar ação ---')  

    def crescer(self, altura):
        try:
            if altura <= 0:
                print('--- Valor inválido ---')
            self.altura += altura
        
        except:
             print('--- Não foi possível realizar ação ---')  

pessoa1= Pessoa('Vitória', 21, 45, 1.60)

print(pessoa1.__dict__)

pessoa1.crescer(0.05)

print(pessoa1.__dict__)