"""
NamedTuple --> Um tupla com nome para ele e parametros
"""

from collections import namedtuple

cachorro = namedtuple('cachorro', ['nome', 'raca', 'idade'])

joao = cachorro(nome = 'Babi', raca = 'pug', idade = 6)

print(joao)

#FORMAS DE ACESSAR
print(joao[1])
print(joao.raca)