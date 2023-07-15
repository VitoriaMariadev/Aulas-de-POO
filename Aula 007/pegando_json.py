import json
from salvando_json import CAMINO_DO_ARQUIVO, Pessoa

with open(CAMINO_DO_ARQUIVO, 'r') as arquivo:
    pessoas = json.load(arquivo)
    p1 = Pessoa(**pessoas[0])

print(p1.nome)