"""
Construindo próprio laço...
"""

def meu_for(iteravel):
    it = iter(iteravel)
    while True:
        try:
            print(next(it))
        except StopIteration:
            break

lista = [1,2,3]
meu_for(lista)