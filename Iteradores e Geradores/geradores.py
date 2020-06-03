"""
Geradores são Iteradores porém o contrário nem sempre é verdade

Geradores podem ser criado por funções geradores
Função geradoras usam a palavra reservada yield

Diferença entre Funções e Funções Geradoras
utiliza retorno           utiliza yield
retorna uma vez           pode usar yield várias vezes
retorna um valor          retorna um gerador
"""

import time

#NÃO É UM GERADOR MAS SIM UMA FUNÇÃO GERADORA
def conta_ate(maximo):
    cont = 1
    while cont <= maximo:
        yield cont
        cont = cont + 1

x = conta_ate(10)
print(next(x))
print(next(x))

for i in x:
    print(i)


#ISSO É MAIS VANTAJOSO POIS COM GERADORES O USO DE MÉMORIA É ABSURDAMENTE MENOR QUE NUMA APLICAÇÃO NORMAL DE FIBONACCI POR EXEMPLO
def seq_feb(qtd_numeros):
    contador = 0
    a, b = 0, 1
    while contador < qtd_numeros:
        a, b = b, a + b
        yield a
        contador += 1

for i in seq_feb(10):
    print(i)

#VELOCIDADE DE UMA GENERATION EXPRESSION COMPARADA COM UM LIST COMPREHENSION

#MAIS RAPIDO
inicio = time.time()
print(sum(num for num in range(10000)))
final = time.time() - inicio
print(final)

inicio2 = time.time()
print(sum([num for num in range(10000)]))
final2 = time.time() - inicio2
print(final2)