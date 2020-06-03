"""
Forma padrão de definir uma função é:

def nome_da_funcao(parametro_de_entrada):
    bloco da função
"""

#EXEMPLO DE UTILIZAÇÃO DE FUNÇÕES
cores = ['azul', 'vermelho', 'amarelo']

#FUNÇÃO INTERAGADA(JÁ VEM COM O PYTHON)
print(cores)

def diz_oi():
    print('Oi!')

diz_oi()

#ISSO É INCOMUM
dizer = diz_oi
dizer()