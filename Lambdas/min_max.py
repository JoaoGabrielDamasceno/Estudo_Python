"""
Max-> maior valor em um iteravel ou em um valor de um ou mais elemento
Min-> menor valor em um iteravel ou em um valor de um ou mais elemento
"""

nomes = ['Ana', 'Joao', 'Gabriel']

print(max(nomes))
print(min(nomes))

print(max(nomes, key=lambda nome: len(nome)))

musica = [
    {'nome': 'Bate o pé', 'tocou': 1},
    {'nome': 'Sugar', 'tocou': 3},
    {'nome': 'Eterna Sacanagem', 'tocou': 2}
]


#IMPRIMIR SO O TITULO
x = {}
x = max(musica, key=lambda musica: musica['tocou'])
print(x['nome'])

#JEITO MAIS BONITO
print(max(musica, key=lambda musica: musica['tocou'])['nome'])