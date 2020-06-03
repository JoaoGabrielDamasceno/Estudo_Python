"""
Mapeamento de valores para um função

Map recebe dois parametros -> primeiro é uma função e o segundo um iterável

Valor só fica na memória até ser utilizado pela primeira vez
"""

import math

def area(raio):
    return math.pi * (raio**2)


raio = [1, 2, 3, 4]
"""
area = map(area, raio)
print(area)
print(list(area))
"""


#MAP COM LAMBDA
area = map(lambda raio: math.pi * (raio**2), raio)
print(area)
print(list(area))

# 9/5 * c + 32

cidades = [('São Paulo', 32), ('Matão', 30), ('Santos', 20)]
c_para_f = lambda dados: (dados[0], (9/5)*dados[1]+32)
print(list(map(c_para_f, cidades)))
