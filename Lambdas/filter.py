"""
-> Filtra dados de uma coleção
Mesmo estilo de map -> uma função e um iterável
"""

import statistics

dados = [1.2, 3.5, 5.1]
media = statistics.mean(dados)

res = filter(lambda valores: valores > media, dados)
print(list(res))

#DADOS FALTANTES
paises = ['', 'Brasil', '', 'Argentina']
res = filter(None, paises)
print(list(res))

#EXEMPLO MAIS COMPLEXO

usuarios = [
    {'username':'Joao', 'tweets': ['Eu sou legal', 'Só queria passar na Bird']},
    {'username':'Carlos', 'tweets': []},
    {'username':'Ana', 'tweets': ['Some corona']}
]

#PRIMEIRA FORMA
#inativos = list(filter(lambda u: len(u['tweets']) == 0, usuarios))

#SEGUNDA FORMA
inativos = list(filter(lambda u:not u['tweets'], usuarios))

print(inativos)

#COMBINANDO FILTER E MAP
nomes = ['Ana', 'Maria', 'Paula']

res = map(lambda nome: f'Sua instrutora é {nome}', filter((lambda y: len(y) < 5), nomes))
print(list(res))