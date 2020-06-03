"""
Assim como map e reduce, recebe dois parâmetros, a função e o iteravel

ex:
lista = [a1, a2, a3... an]
-reduce vai pegar o a1 e a2, aplicar a função e obter r1
-vai pegar r1 e a3 e aplicar a função
.
.
.
No final era retornar UM resultado final

OBS: FUNÇÃO PRECISA DE DOIS PARÂMETROS
"""

from functools import reduce

valores = [1, 2, 3, 4, 5, 6, 7, 8]
mult = lambda x, y: x*y
res = reduce(mult, valores)
print(res)

#LOOP NORMAL (PREFERIVEL)
res = 1
for n in valores:
    res *= n

print(res)