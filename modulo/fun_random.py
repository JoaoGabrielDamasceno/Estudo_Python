"""
Módulo em Python
-São outros arquivos Python
-Módulo Random -> para gerar valores pseudo-aleatórios
"""


"""
FORMA 1
#importanto todo o módulo (todas classes,atributos, funções ficarão disponíveis ou seja, estarão em memória) --> NÃO RECOMENDADO

import random

print(random.random())
"""

"""
#FORMA 2
from random import random

for n in range(10):
    print(random())
"""

"""
from random import uniform

for i in range(10):
    print(uniform(3,7))
"""

"""
from random import randint

for i in range(10):
    print(randint(1,61), end=',')
"""

"""
from random import choice-+

jogada = ['pedra', 'papel', 'tesoura']
print(choice(jogada))
"""

"""
from random import shuffle

pessoas = ['Joao', 'Ana', 'Pedro']
shuffle(pessoas)
print(pessoas[0])
"""

from random import (
    shuffle,
    randint,
    random
)