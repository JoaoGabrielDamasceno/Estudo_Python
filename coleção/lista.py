"""
Vetor/Matriz para armazenar qualquer tipo de dado porém com a vatangem de ser dinâmico
 -Não possue tamanho fixo
 -Dados de tipo aleatorio

 Representadas por colchetes []

 Aceitam valores repetidos
"""

lista1 = [3,2,2,1]

#num = int(input('Qual número deseja procurar?'))
#VER SE UM NÚMEROE ESTÁ NA LISTA
num=5
if num in lista1:
    print('Está na lista!')
else:
    print('Não está na lista!')

#ORDERNAR LISTA
lista1.sort()
print(lista1)

#CONTAR QUANTOS ELEMENTOS TEM EM UMA LISTA
print(f'\n{lista1.count(2)}')

#ADICIONAR VALOR NA LISTA (UM ELEMENTO POR VEZ)
"""
É possível adicionar uma lista na lista, considerado como apenas um paramêtro
lista1.append([1,2,3])
"""
lista1.append(4)
lista1.append("Joao")
print(lista1)

#ADICIONAR VALOR NA LISTA (CADA ELEMENTO DA LISTA COMO VALOR UNICO)
"""
Não é possível um por vez no extend
"""

lista1.extend([2,6,5])
lista1.extend("Gabriel")
print(lista1)

#INSERIR INFORMANDO AONDE VAI SER INSERIDO (Não substitui o valor inicial, é deslocado para a direita)
lista1.insert(2,'Novo valor')
print(lista1)

#JUNTAR DUAS LISTAS
lista2 = ['J','O','A','O']
lista3 = lista1 + lista2
#OU USAR EXTENDS
print(lista3)

#INVERTER LISTA
lista1.reverse()
print(lista1)

#COPIAR LISTA
lista4 = lista1.copy()
print(lista4)

#TAMANHO DA LISTA
print(len(lista1))

#REMOVER ULTIMO ELEMENTO OU PELO INDICE
lista1.pop()
print(lista1)

lista1.pop(2)
print(lista1)

#REMOVER TODOS
lista2.clear()
print(lista2)

#REPETIR UMA LISTA
lista2 = [1,2,3]
lista2 = lista2 * 3
print(lista2)

#TRANSFORMAR STRING EM LISTA, SEPARA PADRÃO POR ESPAÇO MAS DA PARA DEFINIR POR O QUE VAI SER SEPARADO
frase = "João é legal"
frase = frase.split()
print(frase)

#LISTA EM SRING
frase = ' '.join(frase)
print(frase)

"""
carrinho = []
produto = ''
while produto!='sair':
    produto = input('Adicione um produto no carrinho ou digite "sair" para sair: ')
    if produto!='sair':
        carrinho.append(produto)

for elemento in carrinho:
    print(elemento)
"""

"""
Da pra fazer o acesso a cada elemento de forma indexada reversa por é uma lista circular
antes do 0 é -1 e vai até chegar o 0 de novo
"""

cores = ['azul','vermelho','amarelo']
print(cores.index('azul'))

for indice, cor in enumerate(cores):
    print(indice,cor)

cores = list(enumerate(cores))
print(cores)

#ENCONTRAR INDICE ATRAVEZ DE "INDEX" POREM SE TIVER ELEMENTO REPETIDO VAI RETORNAR O PRIMEIRO ENCONTRADO, DA PARA PROCURAR APARTIR DE UM INDICE
#FAZENDO INDEX(VALOR_PROCURADO, INDICE_PARTIDA) OU INDEX(VALOR_PROCURADO, INDICE_PARTIDA, INDICE_PARADA)

#SLICE EM LISTA
lista_slice = [1,2,3,4]

#lista[inicio:fim:passo]
#range(inicio:fim:passo)
print(lista_slice[1:])
print(lista_slice[:2])
print(lista_slice[:-1])
print(lista_slice[1::-1])

print(sum(lista_slice))
print(max(lista_slice))
print(min(lista_slice))

#TRANSFORMAR EM TUPLA
lista_slice = tuple(lista_slice)
print(lista_slice)

#DESMPACOTAMENTO DE LISTA
lista_d = [1,2,3]
v1, v2, v3 = lista_d
print(v1)

#-----IMPORTANTE------
#DEEP COPY OU COPIA PROFUNDA (NÃO ALTERA)
lista0 = [1,2,3]
listac = lista0.copy()

listac.append(4)

print(lista0)
print(listac)

#SHALLOW COPY (ALTERA)

listab = [1,2,3]
listad = listab

listad.append(4)

print(listab)
print(listad)