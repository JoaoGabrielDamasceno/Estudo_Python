"""
->Gerar novas listas com dados processados apartir de iteraveis

[(dado_equação) for dado in lista]
"""

lista = [1,2,3,4,5]

l_comprehension = [num*10 for num in lista]
print(l_comprehension)

def dobro(num):
    return num*2

l_dobro = [dobro(num) for num in lista]
print(l_dobro)

amigos = ['joao', 'maria']
print([nome.title() for nome in amigos])