class Pessoa:
    ano = 2023

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    @classmethod
    def metodo_de_classe(cls): #Chama essa função sem precisar passar alguma parametro
        print('oi')

    @classmethod
    def criar_com_50_anos(cls, nome): #Cria um novo objeto
        return cls(nome, 50)


p2 = Pessoa.criar_com_50_anos('Maria')
print(p2.idade)
Pessoa.metodo_de_classe()