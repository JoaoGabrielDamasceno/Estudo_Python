"""
Bloco whit é usado para se trabalhar o arquivo, após sair desse bloco o arquivo é fechado automaticamente
"""

with open('texto_exemplo.txt') as arquivo:
    print(arquivo.read())

#print(arquivo.read())
