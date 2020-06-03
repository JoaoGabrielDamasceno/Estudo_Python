"""
Evitar KeyError quando procurar um chave que não existe
"""

from collections import defaultdict

dicionario = defaultdict(lambda: 0)

dicionario['chave'] = 'valor'

print(dicionario)

print(dicionario['valor'])

print(dicionario)
