"""
Dicionarios também podem ser lidados em matrizes
{chvae:valor for valor in iteravel}
"""

d = {'a': 1, 'b': 2, 'c': 3}
d_dobro = {chave:valor**2 for chave,valor in d.items()}
print(d_dobro)
