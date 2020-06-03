"""
Listas Aninhadas seriam Matrizes
"""

matriz = [[1,2,3], [4,5,6], [7,8,9]] #MATRIZ 3X3

print(matriz[0][1])

#GERANDO UM TABULEIRO
tabuleiro = [[x for x in range(1,4)] for x in range(1,4)] #FOR DE FORA FEZ AS COLUNAS E O DE DENTRO PREENCHEU AS LINHAS
print(tabuleiro)
