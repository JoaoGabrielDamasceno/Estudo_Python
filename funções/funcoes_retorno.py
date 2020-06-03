"""
return
->finaliza a função
->pode ter varios return em uma função
->retornar qualquer tipo de dado ou até multiplos valores
"""

def quadrado_de_7():
    return 7*7

ret = quadrado_de_7()
print(ret)

def varios_valores():
    return (1,2,3)

n1, n2, n3 = varios_valores()
print(n1,n2,n3)

from random import random

def joga_moeda():
    resultado = random()
    if resultado > 0.5:
        return "Cara"
    return "Coroa"

print(joga_moeda()) 