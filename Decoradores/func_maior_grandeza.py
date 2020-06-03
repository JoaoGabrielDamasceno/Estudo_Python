"""
HOF -> High Ordem Functions (Funções de maior grandeza)

-> Funções que retornam outras funções ou mesmo passar funções como argumentos
"""

from random import choice

def soma(n1, n2):
    return n1 + n2

def dividir(n1,n2):
    return n1/n2

def calcular(n1, n2, funcao):
    return funcao(n1,n2)

print(calcular(1,2,dividir))

#FUNÇÃO DENTRO DE FUNÇÃO

def responda(pessoa):
    def humor():
        return choice(['E ai ', 'Olá ', 'Seja Bem-Vinda '])
    return humor() + pessoa

print(responda('Joao'))