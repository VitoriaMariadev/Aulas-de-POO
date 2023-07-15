import json

CAMINO_DO_ARQUIVO = 'meu_json'

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

p1 = Pessoa('Vitória', 16)
p2 = Pessoa('Maria', 15)
p3 = Pessoa('João', 14)
bd = [p1.__dict__, p2.__dict__, p3.__dict__]

with open(CAMINO_DO_ARQUIVO, 'w') as arquivo:
    json.dump(bd, arquivo, ensure_ascii=False, indent=2)
