class Pessoa:
    ano_atual = 2023

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade #Evita erros caso seja utilizado self.ano_atual


dados = {'nome': 'Vitória', 'idade': 16}  
p1 = Pessoa(**dados) #Desempacotando o dict

print(p1.__dict__)
print(vars(p1))