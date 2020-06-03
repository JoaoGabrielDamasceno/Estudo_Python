"""
Sort() só funciona com listas
Sorted() funciona com qualquer iteravel, sendo que retorna uma lista
"""

numeros = {1,3,5,7,1,2,5,4}
print(sorted(numeros))
print(sorted(numeros, reverse=True))
print(tuple(sorted(numeros)))

usuarios = [
    {'username':'Joao', 'tweets': ['Eu sou legal', 'Só queria passar na Bird']},
    {'username':'Carlos', 'tweets': []},
    {'username':'Ana', 'tweets': ['Some corona']}
]

print(sorted(usuarios, key=lambda usuario: usuario['username']))

musica = [
    {'nome': 'Bate o pé', 'tocou': 1},
    {'nome': 'Sugar', 'tocou': 3},
    {'nome': 'Eterna Sacanagem', 'tocou': 2}
]

print(sorted(musica, key=lambda musica: musica['tocou']))