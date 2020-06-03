"""
Mapas são conhecidos por Dicionarios
"""

receita = {'jan': 100, 'fev': 200, 'mar': 300}

#COMO ITERAR SOB

for chave in receita:
    print(f'{chave} : {receita[chave]}')

print(receita.keys())

#FORMA RECOMENDADA
for chave in receita.keys():
    print(receita[chave])

#DESEMPACOTAMENTO
for chave, valor in receita.items():
    print(f'chave={chave} e valor={valor}')